import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    from pathlib import Path

    data_path = Path("data/features/events.csv")
    df = pd.read_csv(data_path)

    df.head()
    return (df,)


@app.cell
def _(df):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.hist(
        df["duration_minutes"],
        bins=30,
        color="steelblue",
        edgecolor="white",
    )

    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of Events")

    plt.tight_layout()
    fig
    return




if __name__ == "__main__":
    app.run()
