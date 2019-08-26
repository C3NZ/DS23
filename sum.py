import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Summing two numbers together")
    parser.add_argument("num1", type=int)
    parser.add_argument("num2", type=int)
    return parser.parse_args()


if __name__ == "__main__":
    ARGS = get_args()
    print(ARGS.num1 + ARGS.num2)
