
import argparse
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(
        description="Personalized student study tool"
    )
    parser.add_argument("--name", default="World")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    print("Welcome to your study dashboard!")

    tasks = [
        ["Python", "Practice coding"],
        ["Git", "Manage repositories"],
        ["Open Source", "Complete assignments"],
    ]

    print(tabulate(
        tasks,
        headers=["Subject", "Task"],
        tablefmt="fancy_grid"
    ))


if __name__ == "__main__":
    main()
