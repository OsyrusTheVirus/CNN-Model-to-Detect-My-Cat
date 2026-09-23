
import sys

def main() -> None:
    cat_path: str = "./my-cat"
    not_cat_path: str = "./not-my-cat"

    if len(sys.argv) > 1:
        cat_path = sys.argv[1]

    if len(sys.argv) > 2:
        not_cat_path = sys.argv[2]


if __name__ == "__main__":
    main()
