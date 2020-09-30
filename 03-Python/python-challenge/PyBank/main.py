# Modules
import os
import csv

# Path to File
csvpath = os.path.join("Resources", "Budget_Data.csv")

# Lists to store data
def print_calc(budgetdata)
    date = str(budgetdata[0])
    amount = int(budgetdata[1])
    
    # The total number of months
    total_months = date.len()

    # The net total amount of "Profit/Losses" over the entire period


    # The average of the changes in "Profit/Losses" over the entire period


    # The greatest increase in profits (date and amount) over the entire period


    # The greatest decrease in losses (date and amount) over the entire period




# Open the CSVFile
with open(csvpath) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=',')

    # Read the Header Row
    data_header = next(budgetdata)
    print(f"Bank Data: {data_header}")

    def average()


    for row in budgetdata:
        print(row)






