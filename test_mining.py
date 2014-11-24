""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "v2"

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


def test_sample():
    read_stock_data("SAMPLE", "data\SAMPLE.json")

    assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
                                 ('2003/05', 44.67), ('2003/08', 44.63),
                                 ('2003/10', 44.61), ('2003/12', 44.45)]

#####TESTING FOR MISSING KEYS - all currently break the code.
# Need to figure out what the asserts should be before we can fix.####
# def test_no_date_key():
#     read_stock_data("NOKEY_DATE", "data\NOKEY_DATE.json")
#
#     assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2003/05', 44.67), ('2003/08', 44.63),
#                                  ('2003/10', 44.61), ('2003/12', 44.45)]
#
# def test_no_close_key():
#     read_stock_data("NOKEY_CLOSE", "data\NOKEY_DATE.json")
#
#     assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2003/05', 44.67), ('2003/08', 44.63),
#                                  ('2003/10', 44.61), ('2003/12', 44.45)]
#
# def test_no_volume_key():
#     read_stock_data("NOKEY_VOLUME", "data\NOKEY_VOLUME.json")
#
#     assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2003/05', 44.67), ('2003/08', 44.63),
#                                  ('2003/10', 44.61), ('2003/12', 44.45)]

#####TESTING FOR MISSING VALUES - all currently break the code.
# Need to figure out what the asserts should be before we can fix.####
# def test_no_date_value():
#     read_stock_data("NOKEY_DATE", "data\NOKEY_DATE.json")
#
#     assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2003/05', 44.67), ('2003/08', 44.63),
#                                  ('2003/10', 44.61), ('2003/12', 44.45)]
#
# def test_no_close_value():
#     read_stock_data("NOKEY_CLOSE", "data\NOKEY_DATE.json")
#
#     assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2003/05', 44.67), ('2003/08', 44.63),
#                                  ('2003/10', 44.61), ('2003/12', 44.45)]
#
# def test_no_volume_value():
#     read_stock_data("NOKEY_VOLUME", "data\NOKEY_VOLUME.json")
#
#     assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2003/05', 44.67), ('2003/08', 44.63),
#                                  ('2003/10', 44.61), ('2003/12', 44.45)]

######TESTING INVALID VALUES: future date, date with wrong format, date with letters, close
#value with letters, volume with letters
# Need to figure out what the asserts should be before we can fix.####
# def test_invalid_values():
#     read_stock_data("WRONG_VALUES", "data\WRONG_VALUES.json")
#
#     assert six_best_months() == [('2003/06', 44.82), ('2003/11', 44.74),
#                                  ('2003/05', 44.67), ('2003/08', 44.63),
#                                  ('2003/10', 44.61), ('2003/12', 44.45)]


def test_no_file_found():
    with pytest.raises(FileNotFoundError):
        read_stock_data("NOFILE", "data/NOFILE.json")

#we need to decide what we want the file to do with this.
# At the moment it passes because it does happen to return a ValueError,
# but we should have it deliberately rather than accidentally return that.
def test_empty_file():
    with pytest.raises(ValueError):
        read_stock_data("EMPTYFILE", "data/EMPTYFILE.json")

#ditto.
def test_incomplete_file():
    with pytest.raises(ValueError):
        read_stock_data("INCOMPLETE", "data/INCOMPLETE.json")