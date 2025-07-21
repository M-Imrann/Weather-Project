import unittest
from unittest.mock import patch
from weather_fetcher import WeatherFetcher


class TestWeatherFetcher(unittest.TestCase):
    @patch("weather_fetcher.requests.get")
    def test_fetch_weather(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "daily": {
                "time": ["2023-01-01"],
                "temperature_2m_max": [30],
                "temperature_2m_min": [15],
                "temperature_2m_mean": [22.5],
                "wind_speed_10m_max": [10],
                "wind_speed_10m_min": [2],
                "wind_speed_10m_mean": [6]
            }
        }
        fetcher = WeatherFetcher(33.5, 73.1, "2023-01-01", "2023-01-01")
        df = fetcher.fetch()
        self.assertEqual(df.shape[0], 1)
        self.assertIn("temperature_2m_max", df.columns)
        self.assertEqual(df["temperature_2m_max"].iloc[0], 30)
