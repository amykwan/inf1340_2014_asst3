"""
Works with mining.py to visually show best and worst of averaged monthly
stock prices
"""

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann'
__email__ = "eugene.yc.kang@gmail.com, amykwan.cma@gmail.com, " \
            "jessmann74@gmail.com"

__copyright__ = "2014 EKAKJM"
__license__ = "MIT License"

__status__ = "v1"

#imports one per line
from mining import read_stock_data, monthly_averages, \
    six_best_months, six_worst_months


#Visualization
def visualize(stock_name, stock_file_name):
    """
    Takes a set of stock data and prints a list of averaged monthly
    stock prices with highest and lowest average price stocks visually
    indicated.
    :param stock_name: String. Name of a stock company.
    :param stock_file_name: String. Input JSON file name and file location
    of the stock company relative to mining.py
    :return: stock_file_name: Strings. Each month's result appears on a
    separate line in the format "YYYY/MM 111.11" with " <<< One of
    the Best Months" to the right if it is one of the top six months, or
    " <<< One of the Worst Months" to the right if it is one of the bottom
    six months
    """

    #Find the best and worst months
    read_stock_data(stock_name, stock_file_name)
    get_best = six_best_months()
    get_worst = six_worst_months()

    #Print out the lists.
    print("---All Stock Average Prices For ", stock_name)
    print("Month   Average Price")

    for item in monthly_averages:
        result = item[0] + " " + str(item[1])
        if item in get_best:
            result += " <<< One of the Best Months"
        if item in get_worst:
            result += " <<< One of the Worst Months"
            if item in get_best:
                result = item[0] + " " + str(item[1]) + \
                    " <<< Best and Worst overlap"
        print(result)

#One example of visualize using available file
visualize("Google", "data/GOOG.json")
