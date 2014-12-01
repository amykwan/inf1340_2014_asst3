"""
Works with mining.py to compare the standard deviations of two stock
companies' averaged monthly stock prices
"""

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann'
__email__ = "eugene.yc.kang@gmail.com, amykwan.cma@gmail.com, " \
            "jessmann74@gmail.com"

__copyright__ = "2014 EKAKJM"
__license__ = "MIT License"

__status__ = "v2"

#imports one per line
from mining import clean_stock_lists, read_stock_data, monthly_averages
from statistics import *


#Compare Two Stocks Function
def compare_two_stocks(stock_one_name, stock_one_file_name,
                       stock_two_name, stock_two_file_name):
    """
    This function reads in the stock data for two companies and calculates
    the monthly averages and standard deviation for both sets of data.
    :param stock_one_name: String. Name of a stock company.
    :param stock_one_file_name: String. Input JSON file name and file location
    of the stock company relative to mining.py
    :param stock_two_name: String. Name of a second stock company.
    :param stock_two_file_name: String. Input JSON file name and file location
    of second stock company relative to mining.py
    :return: String. Possible values are:
            stock_one_name + " has the highest standard deviation!" or
            stock_one_name + " and " + stock_two_name + " have the same
                standard deviation!" or
            stock_two_name + " has the highest standard deviation!"
    """

    #clean stock list one
    clean_stock_lists()
    #Initialized the average months for each stocks
    read_stock_data(stock_one_name, stock_one_file_name)
    s1_values = [entry[1] for entry in monthly_averages]
    stock_one_std = stdev(s1_values)

    clean_stock_lists()
    read_stock_data(stock_two_name, stock_two_file_name)
    s2_values = [entry[1] for entry in monthly_averages]
    stock_two_std = stdev(s2_values)

    #compare their standard deviations
    if stock_one_std == 0 or stock_two_std == 0:
        return "The standard deviations cannot be compared " \
               "(no data available for one or both of the stocks!"
    elif stock_one_std > stock_two_std:
        return stock_one_name + " has the highest standard deviation!"
    elif stock_one_std == stock_two_std:
        return stock_one_name + " and " + stock_two_name + \
            " have the same standard deviation!"
    else:
        return stock_two_name + " has the highest standard deviation!"
