import unittest
import pandas as pd
from weather_analysis import WeatherAnalyzer, CSVExporter
import os


class TestWeatherAnalyzer(unittest.TestCase):
    '''
    The class is for testing the Weather Analyzer.
    '''
    def setUp(self):
        self.df = pd.DataFrame({
            "time": pd.to_datetime(["2023-01-01", "2023-01-02"]),
            "temperature_2m_max": [30, 32],
            "temperature_2m_min": [10, 12],
            "temperature_2m_mean": [20, 22],
            "wind_speed_10m_max": [5, 6],
            "wind_speed_10m_min": [1, 2],
            "wind_speed_10m_mean": [3, 4],
        })

    def test_analyze(self):
        '''
        Test case for testing the analyze function.
        '''
        analyzer = WeatherAnalyzer(self.df)
        stats, extremes = analyzer.analyze()
        self.assertEqual(stats["Max Temperature"], 32)
        self.assertEqual(extremes["Date Max Temp"].strftime("%Y-%m-%d"),
                         "2023-01-02")

    def test_csv_exporter(self):
        '''
        Test case to test the CSVExporter class
        '''
        path = "output/test_weather.csv"
        CSVExporter.export(self.df, path=path)
        self.assertTrue(os.path.exists(path))
        os.remove(path)
