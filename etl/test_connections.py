import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_connections import get_postgres_engine, get_sqlserver_engine
from sqlalchemy import text  # move this to the top since both functions need it

def test_postgres():
    try:
        engine = get_postgres_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("Postgres Connected:", result.fetchone())
    except Exception as e:
        print("Postgres connection failed:", e)

def test_sqlserver():
    try:
        engine = get_sqlserver_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT @@VERSION;"))
            print("SQL Server Connected:", result.fetchone())
    except Exception as e:
        print("SQL Server connection failed:", e)

if __name__ == "__main__":
    test_postgres()
    test_sqlserver()