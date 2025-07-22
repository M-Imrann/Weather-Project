from arg_parser import ArgParser
from weather_fetcher import WeatherFetcher
from weather_analysis import WeatherAnalyzer, CSVExporter
from plotter import Plotter


class WeatherApp:
    def run(self):
        # Parsing Aruguments
        args = ArgParser().parse_args()

        # Fetching Data
        fetcher = WeatherFetcher(args.lat, args.lon, args.start, args.end)
        df = fetcher.fetch()

        # Analyzing Data
        analyzer = WeatherAnalyzer(df)
        stats, extremes = analyzer.analyze()

        CSVExporter.export(df)

        print("==== Weather Statistics ====")
        for k, v in stats.items():
            print(f"{k}: {round(v, 2)}")

        print("\n==== Extreme Dates ====")
        for k, v in extremes.items():
            print(f"{k}: {v.strftime('%Y-%m-%d')}")

        # Plotting
        Plotter.plot(df, "temperature_2m_mean", "Average Temperature",
                     "Temperature (°C)", "avg_temperature.png")

        Plotter.plot(df, "wind_speed_10m_mean", "Average Wind Speed",
                     "Wind Speed (km/h)", "avg_wind_speed.png")


if __name__ == "__main__":
    WeatherApp().run()
