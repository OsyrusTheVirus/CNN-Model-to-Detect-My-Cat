
import sys
import os

from makedata import MakeData
from model import CNNCatModule

def main() -> None:
    if len(sys.argv) == 1:
        print("\nPlease give path to data.")
        print("Also, make sure directory contains a train and validate subdirectory.")
        print("Example:")
        print("   % make run path=./cat-dataset\n")
        return None

    dataset_path: str = sys.argv[1]

    train_path: str = os.path.join(dataset_path, "train")
    validate_path: str = os.path.join(dataset_path, "validate")

    train_data = MakeData(train_path, True)
    train_data.make_data()
    # train_data.display_tensors()

    validate_data = MakeData(validate_path, False)
    validate_data.make_data()
    # validate_data.display_tensors()

    cat_model = CNNCatModule()
    for epoch in range(20):
        avg_loss = cat_model.train_one_epoch(train_data.get_loader())
        val_acc = cat_model.evaluate(validate_data.get_loader())
        print(f"Epoch {epoch + 1}: loss {avg_loss:.4f}, validate accuracy: {val_acc:.4f}")


if __name__ == "__main__":
    main()
