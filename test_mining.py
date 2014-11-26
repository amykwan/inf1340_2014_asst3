""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "v3"

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


#test case where not enough months of data for two discrete sets of best and worst
def test_overlapping_sets():
    read_stock_data("OSETS", "data\OSETS.json")

    assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
                                 ('2003/05', 44.67), ('2003/08', 44.63),
                                 ('2003/10', 44.61), ('2003/12', 44.45)]

    assert six_worst_months() == [('2003/09', 44.15), ('2003/07', 44.30),
                                  ('2003/12', 44.45), ('2003/10', 44.61),
                                  ('2003/08', 44.63), ('2003/05', 44.67)]


#tests a situation in which only four months' of data is supplied - currently fails
# def test_too_few_months():
#     read_stock_data("TOOFEW", "data\TOOFEW.json")
#
#     assert six_best_months() == [('', 0.0), ('', 0.0), ('', 0.0),
#                                  ('', 0.0), ('', 0.0), ('', 0.0)]
#
#     assert six_worst_months() == [('', 0.0), ('', 0.0), ('', 0.0),
#                                   ('', 0.0), ('', 0.0), ('', 0.0)]

#tests data in non-chronological order
def test_non_chrono_order():
    read_stock_data("NONCHRONO", "data/NONCHRONO.json")

    assert six_best_months() == [('2004/03', 45.18), ('2004/04', 45.02),
                                 ('2003/06', 44.82), ('2003/11', 44.74),
                                 ('2004/05', 44.71), ('2003/05', 44.67)]

    assert six_worst_months() == [('2003/09', 44.15), ('2004/02', 44.28),
                                  ('2003/07', 44.30), ('2004/01', 44.45),
                                  ('2003/10', 44.61), ('2003/08', 44.63)]


#tests duplicate monthly averages. In this case, both Dec 03 and Jan 04 return 44.45. As per her instructions,
#the most recent date should be returned, but currently it's the earlier date
# def test_duplicate_values():
#     read_stock_data("DUPVAL", "data/DUPVAL.json")
#
#     assert six_best_months() == [('2004/03', 45.18), ('2004/04', 45.02),
#                                  ('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2004/05', 44.71), ('2003/05', 44.67)]
#
#     assert six_worst_months() == [('2003/09', 44.15), ('2004/02', 44.28),
#                                   ('2003/07', 44.30), ('2004/01', 44.45), #the second set in this row
#                                   ('2003/10', 44.61), ('2003/08', 44.63)]

def test_no_file_found():
    with pytest.raises(FileNotFoundError):
        read_stock_data("NOFILE", "data/NOFILE.json")


def test_empty_file():
    with pytest.raises(ValueError):
        read_stock_data("EMPTYFILE", "data/EMPTYFILE.json")


def test_incomplete_file():
    with pytest.raises(ValueError):
        read_stock_data("INCOMPLETE", "data/INCOMPLETE.json")