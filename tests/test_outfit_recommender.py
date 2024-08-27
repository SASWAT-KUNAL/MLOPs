import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
                                                
from outfit_recommender import recommend_outfit

class TestOutfitRecommender(unittest.TestCase):
    def test_recommend_outfit(self):
        self.assertEqual(recommend_outfit(30, 'sunny'), "T-shirt and shorts")
        self.assertEqual(recommend_outfit(20, 'cloudy'), "Light jacket and jeans")
        self.assertEqual(recommend_outfit(10, 'rainy'), "Sweater and pants")
        self.assertEqual (recommend_outfit(0, 'snowy'), "Heavy coat, gloves, and scar")

if __name__ == "__main__":
    unittest.main()