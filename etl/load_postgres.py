import pandas as pd
from sqlalchemy import text
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connections import get_postgres_engine

def load_csv_to_postgres():
    # Read extracted CSV files
    users_df = pd.read_csv("users.csv")
    posts_df = pd.read_csv("posts.csv")

    # Connect to Postgres
    engine = get_postgres_engine()

    # Load data into Postgres tables
    with engine.connect() as conn:
        # Optional: Drop tables if re-running
        conn.execute(text("DROP TABLE IF EXISTS users;"))
        conn.execute(text("DROP TABLE IF EXISTS posts;"))

    # Insert users
    users_df.to_sql("users", engine, if_exists="replace", index=False)

    # Insert posts
    posts_df.to_sql("posts", engine, if_exists="replace", index=False)

    print("✅ Data successfully loaded into PostgreSQL!")

if __name__ == "__main__":
    load_csv_to_postgres()