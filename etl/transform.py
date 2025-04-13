import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connections import get_postgres_engine

def transform_data():
    engine = get_postgres_engine()

    # Read users and posts
    users = pd.read_sql("SELECT * FROM users", engine)
    posts = pd.read_sql("SELECT * FROM posts", engine)

    # Join on user ID
    merged = posts.merge(users, left_on='userId', right_on='id', suffixes=('_post', '_user'))

    # Example transformation: Count posts per user
    post_counts = merged.groupby('userId').agg(post_count=('id_post', 'count')).reset_index()

    # Save for next step
    post_counts.to_csv("transformed_post_counts.csv", index=False)

    print("Transformation complete. Saved as transformed_post_counts.csv")

if __name__ == "__main__":
    transform_data()