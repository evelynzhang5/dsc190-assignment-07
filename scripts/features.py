
from pathlib import Path

import pandas as pd


INPUT = Path("data/transformed/events.csv")
OUTPUT = Path("data/features/events.csv")


def main():
    # Load transformed dataset
    df = pd.read_csv(INPUT)

    # Calculate event duration in minutes
    df["duration_minutes"] = df["duration_seconds"] / 60

    # Determine weekday from date
    df["weekday"] = pd.to_datetime(
        df["date"]
    ).dt.day_name()

    # Create output directory
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    # Save features
    df.to_csv(OUTPUT, index=False)

    print(f"Feature rows: {len(df)}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
