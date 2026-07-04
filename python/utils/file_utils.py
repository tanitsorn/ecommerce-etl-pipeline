from pathlib import Path

CLEAN_DATA_PATH = Path("data/clean")

def save_csv(df, filename):
    CLEAN_DATA_PATH.mkdir(parents=True, exist_ok=True)
    df.to_csv(
        CLEAN_DATA_PATH / filename,
        index=False
    )
