from recommender import get_ranked_items
from hot_start import hot_start
import pandas as pd


users = pd.read_csv("data/users.csv")
user_ids = users["user_id"].tolist()

print("HOT START SIMULATION")
hot_result = hot_start(post_id=101, user_ids=user_ids)
print(hot_result)

print("\n📊 RECOMMENDED FEED")
feed = get_ranked_items()
print(feed.head())
