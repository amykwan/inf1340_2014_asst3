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

#initializer
def read_stock_data(stock_name, stock_file_name):



    monthly_averages = []
    #Read the data from the json file
    all_info = read_json_from_file(stock_file_name)

    #Extend the result into the empty list.
    stock_price_process(all_info)


#Helper function which use to get all the monthly average of the stock
def stock_price_process(stock_history):

    #Initialize the variable, list and dictionaries
    result = []
    #Use to store the sum of volume*close price of each day
    monthly_volume_times_close = {}
    #Use to store the sum of volumes
    monthly_volume = {}
    month = ""

    month_in_order = []

    #Loop over all the dictionaries in the json file
    for day_history in stock_history:
        #Take the month and year from the date
        month = day_history["Date"][0:7]
        if month not in month_in_order:
            month_in_order.append(month)
        #Put the volume and price related data into the dictionaries
        if not month in monthly_volume.keys():
            monthly_volume[month] = day_history["Volume"]
            monthly_volume_times_close[month] = \
                day_history["Volume"] * day_history["Close"]
        #if the month is a key for the dictionary, add the value to the existing value of the corresponding month.
        else:
            monthly_volume[month] += day_history["Volume"]
            monthly_volume_times_close[month] += \
                day_history["Volume"] * day_history["Close"]

    #Append all information into a list of tuples.
    for month in month_in_order:
        average = round(monthly_volume_times_close[month]/monthly_volume[month], 2)
        month_byte= unicodedata.normalize('NFKD', month).encode('ascii','ignore')
        month_string = month_byte.decode("utf-8")
        month_string = month_string.replace("-", "/")
        monthly_averages.append((month_string, average))

def six_best_months():
    return get_six_months_by_decision("+")

def six_worst_months():
    return get_six_months_by_decision("-")

#Get the six best/worst month base on the parameter, this is a helper function
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
                #If decision equals to "+", then perform the act of finding the best monthes
                if decision == "+":
                    #Exchange the one on the result list if the average is higher than it
                    if result[count][1] < month_history[1]:
                        old_result = (result[count][0], result[count][1])
                        result[count] = month_history
                        month_history = old_result
                #If decision equals to "+", then perform the act of finding the worst monthes
                elif decision == "-":
                    #Exchange the one on the result list if the average is lower than it
                    if result[count][1] > month_history[1]:
                        old_result = (result[count][0], result[count][1])
                        result[count] = month_history
                        month_history = old_result
    return result

def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
