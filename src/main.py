
import sys
import os

from makedata import MakeData

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
    train_data.display_tensors()

    validate_data = MakeData(validate_path, False)
    validate_data.make_data()
    validate_data.display_tensors()

if __name__ == "__main__":
    main()
