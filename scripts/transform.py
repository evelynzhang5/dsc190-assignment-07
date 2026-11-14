
from pathlib import Path

import pandas as pd


INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")


def main():
    # Load cleaned data
    df = pd.read_csv(INPUT)

    # Extract date from ISO 8601 timestamp
    df["date"] = pd.to_datetime(
        df["timestamp"]
    ).dt.strftime("%Y-%m-%d")

    # Create output directory
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    # Save transformed data
    df.to_csv(OUTPUT, index=False)

    print(f"Transformed rows: {len(df)}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
