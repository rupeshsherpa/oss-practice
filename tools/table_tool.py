
import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table


def main():
    parser = argparse.ArgumentParser(
        description="Server performance monitoring tool"
    )
    parser.add_argument("file", help="Path to the CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.file)

    # Keep servers with high CPU and memory usage
    filtered = df[
        (df["cpu"] >= 70) & (df["memory"] >= 60)
    ]

    table = Table(title="High Resource Usage Servers")

    for column in filtered.columns:
        table.add_column(column)

    for row in filtered.itertuples(index=False):
        table.add_row(*[str(value) for value in row])

    Console().print(table)

    filtered.to_excel("result.xlsx", index=False)
    print("Saved result.xlsx")


if __name__ == "__main__":
    main()
