
from pathlib import Path

import pandas as pd


INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")

VALID_EVENTS = {
    "click",
    "login",
    "purchase",
    "scroll",
    "view",
}


def main():
    # 1. Load the raw dataset
    df = pd.read_csv(INPUT)

    print(f"Original rows: {len(df)}")

    # 2. Drop rows with missing values
    df = df.dropna().copy()

    # 3. Keep only valid event types
    df = df[df["event_type"].isin(VALID_EVENTS)].copy()

    # 4. Convert duration to numeric values
    df["duration_seconds"] = pd.to_numeric(
        df["duration_seconds"],
        errors="coerce",
    )

    # 5. Remove invalid or non-positive durations
    df = df.dropna(subset=["duration_seconds"])
    df = df[df["duration_seconds"] > 0].copy()

    # Keep durations as whole numbers
    df = df[df["duration_seconds"] % 1 == 0].copy()
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    # 6. Parse mixed timestamp formats
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        format="mixed",
        errors="coerce",
    )

    # 7. Remove rows with invalid timestamps
    df = df.dropna(subset=["timestamp"]).copy()

    # 8. Normalize timestamps to ISO 8601
    df["timestamp"] = df["timestamp"].dt.strftime(
        "%Y-%m-%dT%H:%M:%S"
    )

    # 9. Save cleaned dataset
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    print(f"Cleaned rows: {len(df)}")
    print(f"Removed rows: {len(pd.read_csv(INPUT)) - len(df)}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
