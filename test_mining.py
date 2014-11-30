""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "eugene.yc.kang@gmail.com, amykwan.cma@gmail.com, jessmann74@gmail.com, ses@drsusansim.org"

__copyright__ = "2014 EKAKJMSS"
__license__ = "MIT License"

__status__ = "v5"

# imports one per line
import pytest
from mining import *


def test_goog():
    read_stock_data("GOOG", "data\GOOG.json")

    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55),
                                 ('2007/10', 637.38), ('2008/01', 599.42),
                                 ('2008/05', 576.29), ('2008/06', 555.34)]

    assert six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38),
                                  ('2004/10', 164.52), ('2004/11', 177.09),
                                  ('2004/12', 181.01), ('2005/03', 181.18)]


def test_overlapping_sets():
    """
    Tests case where there is not enough months of data for two discrete
    sets of best and worst averages.
    """
    read_stock_data("OSETS", "data\OSETS.json")

    assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
                                 ('2003/05', 44.67), ('2003/08', 44.63),
                                 ('2003/10', 44.61), ('2003/12', 44.45)]

    assert six_worst_months() == [('2003/09', 44.15), ('2003/07', 44.30),
                                  ('2003/12', 44.45), ('2003/10', 44.61),
                                  ('2003/08', 44.63), ('2003/05', 44.67)]



# Not returning in descending order. Not actually specified in PDF but is
#implicit in first test results. Can this be easily updated?
def test_too_few_months():
    """
    Tests case with fewer than six months' worth of data.
    """
    read_stock_data("TOOFEW", "data\TOOFEW.json")

    assert six_best_months() == [('2003/06', 44.82), ('2003/05', 44.67),
                                 ('2003/08', 44.63), ('2003/07', 44.3),
                                 ('', 0.0), ('', 0.0)]

    assert six_worst_months() == [('2003/07', 44.3), ('2003/08', 44.63),
                                  ('2003/05', 44.67), ('2003/06', 44.82),
                                  ('', 0.0), ('', 0.0)]


# Best not returning in descending order. Not actually specified in PDF but is
#implicit in first test results. Can this be easily updated?
def test_non_chrono_order():
    """
    Tests data in non-chronological order.
    """
    read_stock_data("NONCHRONO", "data/NONCHRONO.json")

    assert six_best_months() == [('2004/03', 45.18), ('2004/04', 45.02),
                                 ('2003/06', 44.82), ('2003/11', 44.74),
                                 ('2004/05', 44.71), ('2003/05', 44.67)]

    assert six_worst_months() == [('2003/09', 44.15), ('2004/02', 44.28),
                                  ('2003/07', 44.30), ('2004/01', 44.45),
                                  ('2003/10', 44.61), ('2003/08', 44.63)]


# Best months not returning in descending order; worst months showing duplicate values
def test_duplicate_values():
    """
    Tests duplicate monthly averages; should return most recent of any
    duplicates.
    """
    read_stock_data("DUPVAL", "data/DUPVAL.json")

    assert six_best_months() == [('2004/03', 45.18), ('2004/04', 45.02),
                                 ('2003/06', 44.82), ('2003/11', 44.74),
                                 ('2004/05', 44.71), ('2003/05', 44.67)]

    assert six_worst_months() == [('2003/09', 44.15), ('2004/02', 44.28),
                                  ('2003/07', 44.3), ('2003/12', 44.45),
                                  ('2004/01', 44.45), ('2003/10', 44.61)]


def test_no_file_found():
    """
    Tests case of no json file found at specified location.
    """
    with pytest.raises(FileNotFoundError):
        read_stock_data("NOFILE", "data/NOFILE.json")


def test_empty_file():
    """
    Tests case of a json file with no data in it.
    """
    """
    :return:
    """
    with pytest.raises(ValueError):
        read_stock_data("EMPTYFILE", "data/EMPTYFILE.json")


def test_incomplete_file():
    """
    Tests case with incorrectly formatted JSON data in it.
    """
    with pytest.raises(ValueError):
        read_stock_data("INCOMPLETE", "data/INCOMPLETE.json")
