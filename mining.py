""" Docstring """

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann, Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime
import unicodedata
stock_data = []
monthly_averages = []
current_stock = ""


def read_stock_data(stock_name, stock_file_name):
    """

    :param stock_name:
    :param stock_file_name:
    :return:
    """

    """
        IMO there's no need for a helper function. Just use read stock data.
        Of note: I changed the names of the variables so its more
        english-readable. I was having difficulty parsing the different variables
        when they were all some variation of the word "month".
        Overall the code you wrote for the processing of the data was really good!
        It looks like I changed it but really its just formatting, minor tweaks,
        and making the variable names more differentiated. - Eugene
    """
    # Decode the JSON file to object
    stock_info = read_json_from_file(stock_file_name)

    # Initialize variables, list, dict
    # In format YYYY-MM
    timestamp = ""

    # List of dates [YYYY-MM] that have stock volume and total sales information
    unique_date_list = []
    monthly_volume = {}
    monthly_sales = {}

    # Loop: gathers all the information from ever entry in stock_info
    # creates 2 dict with a key-value pair of [timestamp][value]
    for entry in stock_info:
        # Take month and year from date in format "YYYY-MM"
        # Somewhere in this structure it is assigning MULTIPLE keys to the same value - ex:
        # There are multiple keys with the value "2007-10" for some reason. Probably python
        # is not able to tell if the date written is unique, maybe it's not comparing strings
        # but is instead comparing memory locations
        timestamp = entry["Date"][0:7]

        # The unique_date_list structure is actually not used...
        if timestamp not in unique_date_list:
            unique_date_list.append(timestamp)

        # Puts the volume and total sales into seperate dicts
        if timestamp not in monthly_volume.keys():
            # Establishes key-value pairs
            monthly_volume[timestamp] = entry["Volume"]

        if timestamp not in monthly_sales.keys():
            # Establishes key-value pairs
            monthly_sales[timestamp] = \
                entry["Volume"] * entry["Close"]

        else:
            # Adds to key-value pairs
            # += This does not work with lists, you needs to do:
            # l = []
            # l = l + x
            monthly_volume[timestamp] = monthly_volume[timestamp] + entry["Volume"]
            monthly_sales[timestamp] = \
                monthly_sales[timestamp] + (entry["Volume"] * entry["Close"])

        # Append all information into list of tuples.
        for timestamp in unique_date_list:
            # This isn't happening (below) - Eugene
            #
            avg_monthly_sales = round(monthly_sales[timestamp]/monthly_volume[timestamp], 2)
            month_byte = unicodedata.normalize('NFKD', timestamp).encode('ascii','ignore')
            month_string = month_byte.decode("utf-8")
            month_string = month_string.replace("-", "/")
            monthly_averages.append((month_string, avg_monthly_sales))
            print(timestamp)


    #print(monthly_sales)
    print(unique_date_list)


def six_best_months():
    return get_six_months_by_decision("+")

def six_worst_months():
    return get_six_months_by_decision("-")

#Get the six best/worst month base on the parameter, this is a helper function
"""
    This is going to take me some time to read over. Has bubble-sort
    (or any other sorting methods) been covered in class yet?
    I'm hoping there's an easier way to do it, but if not, this looks like it should work!
"""
def get_six_months_by_decision(decision):
    result = []
    #If the monthly_averages is empty, return a list of empty tuples
    if monthly_averages == [] or decision not in "+-":
        result = [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]

    #Return all the avaiable day averages if the length of the list is less than or equal to 6
    elif len(monthly_averages) <= 6:
        for month_history in monthly_averages:
            result.append(month_history)
        for count in range(6 - len(monthly_averages)):
            result.append(('', 0.0))

    #Check the decision and perform different acts
    else:
        #by here have checked that there is 6 months of data
        #Load the first 6 averages
        for count in range(6):
            result.append(monthly_averages[count])
        #Compare the rest of the averages with the six averages in the result list
        for month_history in monthly_averages[6:]:
            for count in range(6):
                #If decision equals to "+", then perform the act of finding the best months
                if decision == "+":
                    #Exchange the one on the result list if the average is higher than it
                    if result[count][1] < month_history[1]:
                        old_result = (result[count][0], result[count][1])
                        result[count] = month_history
                        month_history = old_result
                #If decision equals to "+", then perform the act of finding the worst months
                elif decision == "-":
                    #Exchange the one on the result list if the average is lower than it
                    if result[count][1] > month_history[1]:
                        old_result = (result[count][0], result[count][1])
                        result[count] = month_history
                        month_history = old_result
    return result

def read_json_from_file(file_name):
    """
    Reads and decodes .json file for use.

    :param file_name: The name of the JSON formatted file that contains stock prices
    :return: Decoded JSON object
    """
    # use a try-catch block when accessing files to ensure that if the file is not found
    # an exception will be thrown.
    # Note: the logic of your statement is fine, its just good to have this. - Eugene
    try:
        with open(file_name) as file_handle:
            file_contents = file_handle.read()
    except FileNotFoundError:
           raise FileNotFoundError("File Not Found!")

    return json.loads(file_contents)
