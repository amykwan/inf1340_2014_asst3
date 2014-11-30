"""
Module to access and return results from mining.py, visualize.py
and compare_two_stocks.py
"""

__author__ = 'Eugene Kang, Amy Kwan, Jessica Mann'
__email__ = "eugene.yc.kang@gmail.com, amykwan.cma@gmail.com, jessmann74@gmail.com"

__copyright__ = "2014 EKAKJM"
__license__ = "MIT License"

__status__ = "v1"

# imports one per line
from mining import read_stock_data, six_best_months, six_worst_months
from compare_two_stocks import compare_two_stocks
from visualize import visualize


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
    while True:
        try:
            company_file = input("Company stock data file: ")
            read_stock_data(company_name, company_file)
            break
        except:
            print("Invalid Input.")
    visit = True
    while visit:
        print("-"*50)
        print("Choose your option")
        print("1. Display the best six months' average stock prices")
        print("2. Display the worst six months' average stock prices")
        print("3. Display all months' average stock prices with best and " +
              "worst six")
        print("4. Display comparison of two companies' monthly average price " +
              "standard deviation")
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
            while True:
                try:
                    second_company_file = input("Second Company file: ")
                    print(compare_two_stocks(company_name, company_file, second_company_name, second_company_file))
                    break
                except:
                    print("Invalid Input.")
        elif option == "5":
            visit = False
        else:
            print("Invalid option selected, please choose again from the \
                following options: ")

#run user interface
if __name__ == "__main__":
    user_interface()
