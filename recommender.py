import pandas as pd

interactions = pd.read_csv("data/interactions.csv")
items = pd.read_csv("data/items.csv")

interactions["timestamp"] = pd.to_datetime(interactions["timestamp"])
interactions["hour"] = interactions["timestamp"].dt.hour

def compute_item_scores(interactions_df):
    scores = {}
    current_hour = 21  # simulate evening

   
    for _, row in interactions_df.iterrows():
        item_id = row["item_id"]
        action = row["action"]
        watch_time = row["watch_time"]

        if item_id not in scores:
            scores[item_id] = 0

        if action == "view":
            scores[item_id] += 1
        elif action == "like":
            scores[item_id] += 3
        elif action == "skip":
            scores[item_id] -= 1

        scores[item_id] += watch_time * 0.1
        
        if abs(row["hour"] - current_hour) <= 1:
           scores[item_id] += 2


    return scores


def get_ranked_items():
    scores = compute_item_scores(interactions)

    score_df = pd.DataFrame(
        scores.items(), columns=["item_id", "score"]
    )

    ranked = score_df.merge(items, on="item_id")
    ranked = ranked.sort_values(by="score", ascending=False)

    return ranked
