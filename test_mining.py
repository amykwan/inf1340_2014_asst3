""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
from mining import *


def test_goog():
    read_stock_data("GOOG", "data\GOOG.json")
    # Note - the assertions will test position 0 of the assertion's list to position 0 of our program's list. Meaning
    # that even if we generate the correct results, if they aren't in the right order the tests will all fail. We need
    # to address this.
    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42),
                                 ('2008/05', 576.29), ('2008/06', 555.34)]
    # The six worst months is incorrect, its missing 2004/08 which has an average sale of 104.66. Adding it, and
    # and dropping the highest month from this set.
    assert six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01),
                                  ('2005/03', 181.18)]

