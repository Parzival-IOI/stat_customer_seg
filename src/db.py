"""SQLite helpers: connect to the database and load the raw orders CSV into it."""

import sqlite3
from pathlib import Path

import pandas as pd

from config import DB_PATH, ORDERS_TABLE, RAW_DATA_PATH


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def load_orders_csv(csv_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(csv_path, index_col=0)
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df


def load_csv_to_sqlite(csv_path: Path = RAW_DATA_PATH, table: str = ORDERS_TABLE) -> int:
    df = load_orders_csv(csv_path)
    with get_connection() as conn:
        df.to_sql(table, conn, if_exists="replace", index=False)
    return len(df)


if __name__ == "__main__":
    n_rows = load_csv_to_sqlite()
    print(f"Loaded {n_rows} rows into {DB_PATH} (table: {ORDERS_TABLE})")
