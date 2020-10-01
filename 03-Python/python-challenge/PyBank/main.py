# Modules
import os
import csv

# Path to File
budgetfile = os.path.join("Resources", "Budget_Data.csv")

total_months = 0
totalpl = 0
change = 0
amount = 0
date = []
pl = []

# Open the CSVFile
with open(budgetfile) as csvfile:

    # Split the data on commas    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip Header Row
    cvsheader = next(csvreader)

    #First Rows
    row1 = next(csvreader)
    total_months += 1
    pl += int(row[1])



    # The total number of months
    total_months = len(budgetdata)
    print(total_months)
    
    for row in budgetdata:
        # The net total amount of "Profit/Losses" over the entire period
        total += float(row[1])
        totalpl = int(total)
        # The average of the changes in "Profit/Losses" over the entire period
    
    
    # The greatest increase in profits (date and amount) over the entire period

    
    # The greatest decrease in losses (date and amount) over the entire period

    
# Print Data

print (f'Financial Analysis')
print (f'___________________')
print (f'Total: ${totalpl}')
print (f'Average Change: $')
print (f'Greatest Increase in Profit:')
print (f'Greatest Decrease in Profits:')


# Set Variable for Output file
output_file = os.path.join("Analysis","Financial_Analysis.csv")

# Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Print in File
    writer.writerows()



