import argparse


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Weather Analyzer"
                                              "using Open-Meteo API")

        self.parser.add_argument("--start", required=True,
                                 help="Start date in YYYY-MM-DD")

        self.parser.add_argument("--end", required=True,
                                 help="End date in YYYY-MM-DD")

        self.parser.add_argument("--lat", type=float,
                                 default=33.528265, help="Latitude")

        self.parser.add_argument("--lon", type=float,
                                 default=73.161513, help="Longitude")

    def parse_args(self):
        return self.parser.parse_args()
