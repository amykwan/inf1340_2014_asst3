""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

import json
import unicodedata

stock_data = []
monthly_averages = []

def clean_stock_lists():
    stock_data.clear()
    monthly_averages.clear()


def read_stock_data(stock_name, stock_file_name):
    """
    This function reads in the entirety of the stock data, decodes it, and
    separates it into two lists of tuples: a list containing total sales by
    month with the equation (Close Price * Volume), and another containing
    total volume of stock sold by month. These values are then used to
    calculate the average price of stock sold via the formula:
        Avg Stock Sold = Monthly Sales / Monthly Volume
    :param stock_name: this parameter is required, but unused in this
        iteration.
    :param stock_file_name: Input JSON file
    :return: unused in this iteration.
    """
    # Ensure that there is no data left over from the previous run
    clean_stock_lists()

    # Decode JSON to object
    stock_info = read_json_from_file(stock_file_name)

    # Create lists for storing data
    unique_date_list = []
    monthly_volume = {}
    monthly_sales = {}

    for entry in stock_info:
        # Create a timestamp in format "YYYY-MM"
        timestamp = entry["Date"][0:7]

        # Check if timestamp already exists, if not add to list
        if timestamp not in unique_date_list:
            unique_date_list.append(timestamp)

        # Check if timestamp is already a key in the monthly_volume list,
        # if not add.
        if timestamp not in monthly_volume.keys():
            monthly_volume[timestamp] = entry["Volume"]

        # Check if timestamp is already a key in the monthly_sales list,
        # if not add.
        if timestamp not in monthly_sales.keys():
            monthly_sales[timestamp] = entry["Volume"] * entry["Close"]

        # Total value of sales and volume into lists
        else:
            monthly_volume[timestamp] = monthly_volume[timestamp] + \
                entry["Volume"]
            monthly_sales[timestamp] = monthly_sales[timestamp] + \
                entry["Volume"] * entry["Close"]

    # Calculate average monthly sales, and change the date format to "YYYY/MM"
    # Append to the monthly_averages list
    for date in unique_date_list:
        avg_monthly_sales = round(monthly_sales[date]/monthly_volume[date], 2)
        month_byte = unicodedata.normalize('NFKD', date).encode('ascii',
                                                                'ignore')
        month_string = month_byte.decode("utf-8")
        month_string = month_string.replace("-", "/")
        monthly_averages.append((month_string, avg_monthly_sales))
    return


def six_best_months():
    """
    This function produces the best six months of average stock price.
    :return: The best six months of average stock price in a list of tuples, in
    the format('YYYY/DD', 111.11)
    """
    result = validate_averages()
    # If data was validated, sort and order from highest to lowest starting at
    # index 0
    if "Validated" in result:
        sorted_best_avg = (sorted(monthly_averages, key=lambda tup: tup[1],
                                  reverse=True))
        return sorted_best_avg[0:6]

    # If data was not validated, return the result passed to this function.
    else:
        return result


def six_worst_months():
    """
    This function produces the worst six months of average stock price.
    :return: The worst six months of average stock price in a list of tuples,
    in the format ('YYYY/DD', 111.11)
    """
    result = validate_averages()
    # If data was validated, sort and order from lowest to highest starting at
    # index 0
    if "Validated" in result:
        sorted_worst_avg = (sorted(monthly_averages, key=lambda tup: tup[1],
                                   reverse=False))
        return sorted_worst_avg[0:6]

    # If data was not validated, return the result passed to this function.
    else:
        return result


def validate_averages():
    """
    This function validates the monthly averages list to ensure that it has a
    full range of entries to sort through. If not, it will either return all
    zero values, or it will take what values it can and enter it into a list,
    and then return zero values.
    :return: If the data is incomplete, a list of six months, if data is
     complete it will
    insert the string "Validated" into the list and return that.
    """
    result = []

    # If monthly averages is empty, return a "blank" result.
    if monthly_averages is []:
        result = [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0),
                  ('', 0.0)]

    # If the monthly averages data is incomplete (less than 6) fill the
    # remaining empty slots with zeroes
    elif len(monthly_averages) <= 6:
        for entry in monthly_averages:
            result.append(entry)
        for count in range(6 - len(monthly_averages)):
            result.append(('', 0.0))

    # Otherwise return validated
    else:
        result.append("Validated")
    return result


def read_json_from_file(file_name):
    """
    Reads and decodes .json file for use.

    :param file_name: The name of the JSON formatted file that contains
    stock prices
    :return: Decoded JSON object
    """

    try:
        with open(file_name) as file_handle:
            file_contents = file_handle.read()
    except FileNotFoundError:
        raise FileNotFoundError("File Not Found!")
    except ValueError:
        raise ValueError("This file is empty or not in the correct format!")
    return json.loads(file_contents)
