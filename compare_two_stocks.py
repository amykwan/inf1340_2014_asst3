"""
Works with mining.py to compare the standard deviations of two stock
companies' averaged monthly stock prices
"""

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann'
__email__ = "eugene.yc.kang@gmail.com, amykwan.cma@gmail.com, " \
            "jessmann74@gmail.com"

__copyright__ = "2014 EKAKJM"
__license__ = "MIT License"

__status__ = "v1"

#imports one per line
from mining import clean_stock_lists, read_stock_data, monthly_averages


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
    stock_one = monthly_averages[:]
    stock_one_std = get_standard_deviation(stock_one)

    #clean stock list two
    clean_stock_lists()
    read_stock_data(stock_two_name, stock_two_file_name)
    stock_two = monthly_averages[:]
    stock_two_std = get_standard_deviation(stock_two)

    #compare their standard deviations
    if stock_one_std > stock_two_std:
        return stock_one_name + " has the highest standard deviation!"
    elif stock_one_std == stock_two_std:
        return stock_one_name + " and " + stock_two_name + \
            " have the same standard deviation!"
    else:
        return stock_two_name + " has the highest standard deviation!"


#Helper Function for finding the standard deviation
def get_standard_deviation(stock_info):
    """
    Takes monthly stock averages and calculates the mean value base
    to return the standard deviation for the list
    :param: stock_info: A list of tuples in the format('YYYY/DD', 111.11)
    where 'YYYY/DD' represents the month for which stocks were averaged
    and 111.11 represents the averaged stock for that month.
    :return: Float. Standard deviation for the monthly averages.
    """
    standard_deviation = 0.0
    total = 0.0

    #Finding the mean value base on the average values of all months
    for item in stock_info:
        total += item[1]
    mean = total/len(stock_info)

    deviations = []

    #Find the standard deviations
    for item in stock_info:
        deviations.append(item[1] - mean)
    for deviation in deviations:
        standard_deviation += deviation**2
    std_deviation = standard_deviation/len(stock_info)

    return std_deviation

#One example of compare two stocks using available files
print(compare_two_stocks("GOOG", "data/GOOG.json",
                         "TSE-SO", "data/TSE-SO.json"))
