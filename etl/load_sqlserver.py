import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connections import get_sqlserver_engine

def load_to_sql_server():
    # Read the transformed CSV
    df = pd.read_csv("transformed_post_counts.csv")

    # Connect to SQL Server
    engine = get_sqlserver_engine()

    # Load the data into a new table
    df.to_sql("user_post_counts", engine, if_exists="replace", index=False)

    print("Transformed data loaded into SQL Server!")

if __name__ == "__main__":
    load_to_sql_server()