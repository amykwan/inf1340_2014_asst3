""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "v1"

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