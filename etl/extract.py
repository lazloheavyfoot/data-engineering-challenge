import requests
import pandas as pd

def extract_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    return pd.DataFrame(response.json())

def extract_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    return pd.DataFrame(response.json())

if __name__ == "__main__":
    users_df = extract_users()
    posts_df = extract_posts()

    # Save locally for inspection / staging
    users_df.to_csv("users.csv", index=False)
    posts_df.to_csv("posts.csv", index=False)
    print("✅ Data extracted and saved to users.csv and posts.csv")