import unittest
import pandas as pd
import os
from plotter import Plotter


class TestPlotter(unittest.TestCase):
    '''
    The class is for to write the test cases to test graphs
    '''
    def setUp(self):
        self.df = pd.DataFrame({
            "time": pd.to_datetime(["2023-01-01", "2023-01-02"]),
            "temperature_2m_mean": [20, 21],
            "wind_speed_10m_mean": [5, 6]
        })

    def test_plot_temperature(self):
        '''
        Test case to test the temperature graph
        '''
        path = "output/plots/test_temp.png"
        Plotter.plot(self.df, "temperature_2m_mean", "Test Temp",
                     "Temp", "test_temp.png")
        self.assertTrue(os.path.exists(path))
        os.remove(path)

    def test_plot_wind(self):
        '''
        Test case to test the wind graph
        '''
        path = "output/plots/test_wind.png"
        Plotter.plot(self.df, "wind_speed_10m_mean", "Test Wind", "Wind",
                     "test_wind.png")
        self.assertTrue(os.path.exists(path))
        os.remove(path)
