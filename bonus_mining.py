""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "v7"

import json
import unicodedata
import re

stock_data = []
monthly_averages = []


def clean_stock_lists():
    global monthly_averages
    global stock_data
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
    :param stock_name: String. this parameter is required, but unused in this
        iteration.
    :param stock_file_name: String. Input JSON file name and file location
    relative to mining.py
    :return: A list of tuples. Each tuple contains valid months in the stock
    data and its average stock sold in that month the format('YYYY/DD', 111.11)
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
        timestamp = "0000-00"
        if "Date" in entry.keys():
            timestamp = entry["Date"][0:7]
        else:
            r = re.compile('.*-.*-.*')
            for key in entry.keys():
                if r.match(str(entry[key])):
                    timestamp = entry[key][0:7]

        close_price = 0.0
        if "Close" in entry.keys():
            close_price = entry["Close"]
        else:
            close_price = entry[""]

        volume = 0.0
        if "Volume" in entry.keys():
            volume = entry["Volume"]
        else:
            volume = entry[""]

        # Check if timestamp already exists, if not add to list
        if timestamp not in unique_date_list:
            unique_date_list.append(timestamp)

        # Check if timestamp is already a key in the monthly_volume list,
        # if not add.
        if timestamp not in monthly_volume.keys():
            monthly_volume[timestamp] = volume

        # Check if timestamp is already a key in the monthly_sales list,
        # if not add.
        if timestamp not in monthly_sales.keys():
            monthly_sales[timestamp] = volume * close_price

        # Total value of sales and volume into lists
        else:
            monthly_volume[timestamp] = monthly_volume[timestamp] + \
                volume
            monthly_sales[timestamp] = monthly_sales[timestamp] + \
                volume * close_price

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
    :param: A list of tuples. Each tuple contains valid months in the stock
    data and its average stock sold in that month the format('YYYY/DD', 111.11)
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
    :param: A list of tuples. Each tuple contains valid months in the stock
    data and its average stock sold in that month the format('YYYY/DD', 111.11)
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
    :param: A list of tuples. Each tuple contains valid months in the stock
    data and its average stock sold in that month the format('YYYY/DD', 111.11)
    :return: If the data is incomplete, a list of six months with tuples
     in the format ('', 0.0).
     Or if data is complete it will insert the string "Validated" into the
     list and return the updated list.
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
        return stock_one_name + " and " + stock_two_name + " have the same standard deviation!"
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
        if item in get_best:
            print(item[0] + " " + str(item[1]) + " <<< One of the Best Months")
        elif item in get_worst:
            print(item[0] + " " + str(item[1]) + " <<< One of the Worst Months")
        else:
            print(item[0] + " " + str(item[1]))


def user_interface():
    """
    Prompts for stock data input and offers options to perform calculations
    on data: best six, worst six, all months' average stock prices with best
    and worst visually indicated, and comparing two company's standard
    deviation of monthly average price.

    :inputs: company_name: String. Name of a stock company.
    :inputs: company_file: String. Input JSON file name and file location
    of the stock company relative to mining.py
    :inputs: option: integer between 1 and 5
    :inputs: second_company_name: String. Name of a second stock company.
    :inputs: second_company_file: String. Input JSON file name and file
    location of the second stock company relative to mining.py

    :returns: If option 1 is selected returns the top six months of average
    stock price in a list of tuples, in the format('YYYY/DD', 111.11)

    If option 2 is selected returns the top six months of average
        stock price in a list of tuples, in the format('YYYY/DD', 111.11).

    If option 3 is selected returns first company's monthly average stock
        price appears on a separate line in the format "YYYY/MM 111.11" with
        " <<< One of the Best Months" to the right if it is one of the top
        six months, or " <<< One of the Worst Months" to the right if it is
        one of the bottom six months.

    If option 4 is selected prints one of three options:
        1. stock_one_name + " has the highest standard deviation!" or
        2. stock_one_name + " and " + stock_two_name + " have the same
                standard deviation!" or
        3. stock_two_name + " has the highest standard deviation!"

    If an integer outside of 1 to 6 is entered for option, a prompt prints:

    """
    company_name = input("Company name: ")
    company_file = input("Company stock data file: ")
    visit = True
    read_stock_data(company_name, company_file)
    while visit:
        print("-"*50)
        print("Choose your option")
        print("1. Display the best six months' average stock prices")
        print("2. Display the worst six months' average stock prices")
        print("3. Display all months' average stock prices with best and \
                worst six")
        print("4. Display comparison of two companies' monthly average price \
                standard deviation")
        print("5. Exit")
        option = (input("Choose: "))
        if option == "1":
            print(six_best_months())
        elif option == "2":
            print(six_worst_months())
        elif option == "3":
            visualize(company_name, company_file)
        elif option == "4":
            second_company_name = input("Second Company name: ")
            second_company_file = input("Second Company stock data file: ")
            print(compare_two_stocks(company_name, company_file,
                                     second_company_name, second_company_file))
        elif option == "5":
            visit = False
        else:
            print("Invalid option selected, please choose again from the \
                following options: ")

#Delete this line if you want to run test_mining
user_interface()
