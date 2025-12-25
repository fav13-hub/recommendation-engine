# Recommendation Engine MVP

Welcome to the **Recommendation Engine MVP** ,a minimum viable product for a personalized recommendation system designed for a commerce startup.  
This project simulates TikTok-like recommendations for shopping content using dummy data. The system ranks posts, predicts engagement, and personalizes feeds to enhance user experience.

---

## 🌟 Project Overview

The goal of this MVP is to:

- Demonstrate how a recommendation system can rank content dynamically
- Simulate user behavior to test scoring logic
- Provide a foundation to integrate with real backend data
- Explore personalization, viral logic, and engagement-based scoring

This project focuses on **data-driven recommendations** and sets up the infrastructure for more advanced machine learning models in the future.

---

## 📂 Folder Structure

recommendation-engine/
├── data/
│ ├── interactions.csv # Simulated user actions: view, like, skip, orders, watch_time
│ ├── items.csv # Item metadata: item_id, name, category, etc.
│ └── users.csv # User metadata: user_id, location, subscription, etc.
├── recommender.py # Core functions for computing item scores
├── hot_start.py # Optional module for viral hot-start logic
├── main.py # Entry point to run the recommendation system
├── requirements.txt # Python dependencies
└── README.md # Project overview


---

## ⚙️ Features

1. **Engagement-based Scoring**  
   - Each post is scored based on user interactions: views, likes, shares, skips, orders, and watch time.  

2. **Time-of-Day Boost**  
   - Posts are boosted if interactions happen at specific hours to simulate contextual relevance.  

3. **Hot-Start Viral Logic**  
   - New posts are shown to a small test group first. If engagement is high, the post is gradually shown to more users.  

4. **Ranked Feed**  
   - Items are ranked by computed scores and merged with item metadata to create a personalized feed.  

5. **MVP Ready for Backend Integration**  
   - Currently uses dummy CSV data. Once connected to real backend data, it can process live interactions.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/fav13-hub/recommendation-engine.git
cd recommendation-engine
Install dependencies:

bash
Copy code
pip install -r requirements.txt
🚀 Usage
Run the recommendation system using:

bash
Copy code
python main.py
The system reads the CSV files in the data/ folder

Computes scores for each item

Produces a ranked list of items based on engagement and time-based boosts