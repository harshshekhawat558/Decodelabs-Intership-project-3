import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Source_Code"))
from recommender import Recommender, tokenize, jaccard_similarity

class RecommenderTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            {"id": 1, "name": "Python", "description": "python coding beginner", "popularity": 90},
            {"id": 2, "name": "ML", "description": "python machine learning data", "popularity": 80},
            {"id": 3, "name": "Design", "description": "html css design", "popularity": 70},
        ]

    def test_tokenize_is_case_insensitive(self):
        self.assertEqual(tokenize("Python CODE"), {"python", "code"})

    def test_jaccard_similarity(self):
        self.assertAlmostEqual(jaccard_similarity({"a", "b"}, {"b", "c"}), 1/3)

    def test_excludes_liked_items(self):
        result = Recommender(self.items).recommend([1], 5)
        self.assertTrue(all(x["item"]["id"] != 1 for x in result))

    def test_returns_requested_limit(self):
        result = Recommender(self.items).recommend([1], 1)
        self.assertEqual(len(result), 1)

    def test_popularity_fallback_without_history(self):
        result = Recommender(self.items).recommend([], 1)
        self.assertEqual(result[0]["id"], 1)

    def test_invalid_weights_raise_error(self):
        with self.assertRaises(ValueError):
            Recommender(self.items, 0.7, 0.4)

if __name__ == "__main__":
    unittest.main()
