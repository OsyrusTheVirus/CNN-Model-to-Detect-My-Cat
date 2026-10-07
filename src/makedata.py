import torch
import os
from PIL import Image, ImageOps
from torchvision.transforms import v2
from torchvision import datasets
from torchvision.utils import save_image
from torch.utils.data import DataLoader


class MakeData:

    def __init__(self, path: str, augment: bool):
        self.path: str = path
        self.loader: DataLoader = None
        self.augment: bool = augment

        transform_list = [
            v2.Resize((64, 64)),                   # shrinks aspect ratio to value x value
            v2.ToImage(),                          # turns PIL image into tensor (array) of integers 0 (min) to 255 (max)
            v2.ToDtype(torch.float32, scale=True), # turns values from 0 to 255 to 0.0 to 1.0 (dividing by 255)
        ]

        if self.augment:
            # augmentation transformations
            transform_list.append(v2.RandomHorizontalFlip(p=0.5))
            transform_list.append(v2.RandomRotation(degrees=15))
            transform_list.append(v2.ColorJitter(brightness=0.3, contrast=0.3))

        transform_list.append(v2.Normalize(mean=[0.5]*3, std=[0.5]*3))

        self.transformer = v2.Compose(transform_list)

    def __load_image(self, path) -> Image.Image:
        img = Image.open(path)               # open image
        img = ImageOps.exif_transpose(img)   # fix phone-photo orientation
        return img.convert("RGB")
    
    def make_data(self) -> None:
        """
        Applies transformers on data
        """
        partyset = datasets.ImageFolder(self.path, transform=self.transformer, loader=self.__load_image)
        self.loader = DataLoader(partyset, batch_size=20, shuffle=self.augment)

    def get_loader(self) -> DataLoader | None:
        """
        Returns tensors held within DataLoader
        """
        return self.loader

    def display_tensors(self):
        """
        Print and displays contents of this MakeData object.
        """
        print(self.path)

        if self.loader is None:
            print("No tensors have been made.")
            return None
        
        dir_path: str = "./makedata-batched-images/" + self.path
        os.makedirs(dir_path, exist_ok=True)

        count = 0
        for image, label in self.loader:
            print(str(image.shape) + " " + str(image.dtype) + ", label: " + str(label))

            image_name: str = "party_grid" + str(count) + ".png"
            image_path: str = os.path.join(dir_path, image_name)
            save_image(image, image_path, nrow=4, normalize=True)
            count += 1
            