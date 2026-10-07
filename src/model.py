import torch
from torch import nn
from torch.utils.data import DataLoader


class CNNCatModule(nn.Module):
    def __init__(self):
        super().__init__()  

        self.features = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(4096, 64),
            nn.ReLU(),
            nn.Linear(64, 2),
        )

        self.loss_fn = nn.CrossEntropyLoss()    # for calculating correctness of epoch
        self.optimizer = torch.optim.Adam(self.parameters(), lr=0.001) # optimizing training

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

    def train_one_epoch(self, loader: DataLoader) -> float:
        self.train()  # tells model to begin training
        total_loss = 0.0 # total loss across epochs

        for images, labels in loader:
            outputs = self(images)                  # attempt to guess
            loss = self.loss_fn(outputs, labels)    # measure the error
            self.optimizer.zero_grad()              # clear the previous gradient
            loss.backward()                         # get the gradient, or tune to get fewer mistakes (backpropagation)
            self.optimizer.step()                   # update the weights based on the gradient

            total_loss += loss.item()

        return total_loss / len(loader)  # average loss for the epoch

    def evaluate(self, loader: DataLoader) -> float:
        self.eval()
        correct = 0
        total = 0

        with torch.no_grad():  # do not include gradients
            for images, labels in loader:
                predictions = self(images).argmax(dim=1)
                correct += (predictions == labels).sum().item()
                total += len(labels)


        return correct / total
            


if __name__ == "__main__":
    model = CNNCatModule()
    print(model)  # shows every layer

    fake_batch = torch.randn(1, 3, 64, 64)  # 1 random "image"
    output = model(fake_batch)              # calls forward() for you
    print(output.shape)                     # want: torch.Size([1, 2])

    total = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {total:,}")