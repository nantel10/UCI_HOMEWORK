# Modules
import os
import csv

# Path to File
budgetfile = os.path.join("Resources", "Budget_Data.csv")

total = 0
avgchange = 0

# Open the CSVFile
with open(budgetfile) as csvfile:

    # Split the data on commas    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip Header Row
    next(csvreader)

    budgetdata = list(csvreader)

    # The total number of months
    total_months = len(budgetdata)
    print(total_months)

   
    
    for row in budgetdata:
        # The net total amount of "Profit/Losses" over the entire period
        total += float(row[1])
        
        # The average of the changes in "Profit/Losses" over the entire period
        avgchange = average(row[1])

    totalpl = int(total)
    print (f'Total: {totalpl}')
    print (f'Average: {avgchange}')



# Define function 
    


   


    # The net total amount of "Profit/Losses" over the entire period


    


    # The greatest increase in profits (date and amount) over the entire period


    # The greatest decrease in losses (date and amount) over the entire period





    
    # Print Data
    #print(f"Total Months in Data: {total_months}")





