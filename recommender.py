"""Simple hybrid AI-style recommendation logic using content and popularity."""
import re
from collections import Counter

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def jaccard_similarity(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)

class Recommender:
    def __init__(self, items, content_weight=0.8, popularity_weight=0.2):
        if abs(content_weight + popularity_weight - 1.0) > 1e-9:
            raise ValueError("Weights must add up to 1.0")
        self.items = items
        self.content_weight = content_weight
        self.popularity_weight = popularity_weight

    def recommend(self, liked_item_ids, limit=5):
        liked = [item for item in self.items if item["id"] in liked_item_ids]
        if not liked:
            return sorted(
                [i for i in self.items if i["id"] not in liked_item_ids],
                key=lambda x: x.get("popularity", 0), reverse=True
            )[:limit]

        profile = set().union(*(tokenize(i["description"]) for i in liked))
        candidates = []
        max_pop = max((i.get("popularity", 0) for i in self.items), default=1) or 1

        for item in self.items:
            if item["id"] in liked_item_ids:
                continue
            similarity = jaccard_similarity(profile, tokenize(item["description"]))
            popularity = item.get("popularity", 0) / max_pop
            score = (self.content_weight * similarity +
                     self.popularity_weight * popularity)
            candidates.append((score, item))

        candidates.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
        return [{"item": item, "score": round(score, 4)}
                for score, item in candidates[:limit]]

if __name__ == "__main__":
    catalog = [
        {"id": 1, "name": "Python Basics", "description": "python coding programming beginner", "popularity": 90},
        {"id": 2, "name": "Machine Learning", "description": "machine learning python data models", "popularity": 85},
        {"id": 3, "name": "Web Design", "description": "html css design frontend", "popularity": 70},
        {"id": 4, "name": "Data Science", "description": "python data analysis statistics", "popularity": 80},
        {"id": 5, "name": "Photography", "description": "camera photography editing", "popularity": 60},
    ]
    engine = Recommender(catalog)
    for result in engine.recommend([1], limit=3):
        print(result["item"]["name"], result["score"])
