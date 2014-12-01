"""
Module to test compare_two_stocks.py
"""

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann'
__email__ = "eugene.yc.kang@gmail.com, amykwan.cma@gmail.com, " \
            "jessmann74@gmail.com"

__copyright__ = "2014 EKAKJM"
__license__ = "MIT License"

__status__ = "v2"

#imports one per line
import pytest
from mining import *
from compare_two_stocks import *


def test_comparison():
    """
    Tests the comparison between two stocks.
    """

    assert (compare_two_stocks("GOOG",
                               "data/GOOG.json", "TSE-SO",
                               "data/TSE-SO.json"))\
        == "GOOG has the highest standard deviation!"


def test_missing_stocks():
    """
    Tests to check that an error is thrown when only one stock is available.
    """
    # 1 Empty JSON error test
    with pytest.raises(ValueError):
        compare_two_stocks("GOOG", "data/GOOG.json", "EMTY",
                           "data/EMPTYFILE.json")

    with pytest.raises(FileNotFoundError):
        compare_two_stocks("NOFILE", "data/NOFILE.json", "TSE-SO",
                           "data/TSE-SO.json")
