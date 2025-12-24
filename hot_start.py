import random

def hot_start(post_id, user_ids, threshold=0.2):
    test_group = random.sample(user_ids, min(10, len(user_ids)))

    engagement_rate = random.uniform(0, 1)

    if engagement_rate >= threshold:
        next_reach = 1000
    else:
        next_reach = 10

    return {
        "post_id": post_id,
        "test_group_size": len(test_group),
        "engagement_rate": round(engagement_rate, 2),
        "next_reach": next_reach
    }
