import unittest
from unittest.mock import patch
import argparse
from arg_parser import ArgParser


class TestArgParser(unittest.TestCase):
    @patch("argparse.ArgumentParser.parse_args",
           return_value=argparse.Namespace(start="2023-01-01",
                                           end="2023-01-05",
                                           lat=12.34, lon=56.78))
    def test_parse_args(self, mock_args):
        parser = ArgParser()
        args = parser.parse_args()
        self.assertEqual(args.start, "2023-01-01")
        self.assertEqual(args.end, "2023-01-05")
        self.assertEqual(args.lat, 12.34)
        self.assertEqual(args.lon, 56.78)
