from typing import *
from dataclasses import dataclass
import unittest
import math


calpoly_email_addresses = ["mpkerner@calpoly.edu"]

@dataclass
class GlobeRect:
    lo_lat: int
    hi_lat: int
    west_long: int
    east_long: int

@dataclass
class Region:
    rect: 'GlobeRect'
    region_name: str
    terrain: str

@dataclass
class RegionCondition:
    region: 'Region'
    year: int
    pop: int
    ghg_rate: int




# put all test cases in the "Tests" class.
class Tests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(14,14)


if (__name__ == '__main__'):
    unittest.main()