"""Central configuration loaded from environment variables (.env)."""

from pathlib import Path

from dotenv import load_dotenv
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

DB_PATH = PROJECT_ROOT / os.getenv("DB_PATH", "data/customer_seg.db")
RAW_DATA_PATH = PROJECT_ROOT / os.getenv("RAW_DATA_PATH", "materials/rfm_data_orders.rda.csv")
ORDERS_TABLE = os.getenv("ORDERS_TABLE", "orders")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
