"""Entry point: ensure the orders DB is populated and build the base RFM table."""

import sqlite3

import pandas as pd

from config import DB_PATH, ORDERS_TABLE
from db import get_connection, load_csv_to_sqlite


def ensure_data_loaded() -> None:
    if not DB_PATH.exists():
        load_csv_to_sqlite()
        return
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (ORDERS_TABLE,)
        )
        if cursor.fetchone() is None:
            load_csv_to_sqlite()


def load_orders() -> pd.DataFrame:
    with get_connection() as conn:
        df = pd.read_sql(f"SELECT * FROM {ORDERS_TABLE}", conn, parse_dates=["order_date"])
    return df


def build_rfm_table(orders: pd.DataFrame, snapshot_date: pd.Timestamp | None = None) -> pd.DataFrame:
    snapshot_date = snapshot_date or orders["order_date"].max() + pd.Timedelta(days=1)
    rfm = orders.groupby("customer_id").agg(
        recency=("order_date", lambda s: (snapshot_date - s.max()).days),
        frequency=("order_date", "count"),
        monetary=("revenue", "sum"),
    )
    return rfm.reset_index()


def main() -> None:
    ensure_data_loaded()
    orders = load_orders()
    rfm = build_rfm_table(orders)

    print(f"Orders loaded: {len(orders)} rows, {orders['customer_id'].nunique()} customers")
    print(rfm.describe())


if __name__ == "__main__":
    main()
