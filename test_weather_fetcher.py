

import unittest
from src.weather_fetcher import get_weather

class TestWeatherFetcher(unittest.TestCase):
    def test_get_weather(self):
        temp, description = get_weather()
        
        self.assertIsInstance(temp, (int, float), "Temperature: ")
        self.assertIsInstance(description, str, "Weather: ")
        
if __name__ == "__main__":
    unittest.main()