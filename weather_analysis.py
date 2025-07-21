import pandas as pd


class WeatherAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        '''
        Analyze the max, min, average temperature at 2m and wind speed at 10m
        '''
        stats = {
            "Max Temperature": self.df["temperature_2m_max"].max(),
            "Min Temperature": self.df["temperature_2m_min"].min(),
            "Avg Temperature": self.df["temperature_2m_mean"].mean(),
            "Max Wind Speed": self.df["wind_speed_10m_max"].max(),
            "Min Wind Speed": self.df["wind_speed_10m_min"].min(),
            "Avg Wind Speed": self.df["wind_speed_10m_mean"].mean(),
        }
        extremes = {
            "Date Max Temp": self.df.loc[self.df["temperature_2m_max"]
                                         .idxmax(), "time"],
            "Date Min Temp": self.df.loc[self.df["temperature_2m_min"]
                                         .idxmin(), "time"],
            "Date Max Wind": self.df.loc[self.df["wind_speed_10m_max"]
                                         .idxmax(), "time"],
            "Date Min Wind": self.df.loc[self.df["wind_speed_10m_min"]
                                         .idxmin(), "time"],
        }
        return stats, extremes


class CSVExporter:
    '''
    Exports the data in csv file in output directory
    '''
    @staticmethod
    def export(df: pd.DataFrame, path="output/weather_data.csv"):
        import os
        os.makedirs("output", exist_ok=True)
        df.to_csv(path, index=False)
