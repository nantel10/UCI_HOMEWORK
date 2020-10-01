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
    rowone = next(csvreader)
    total_months += 1
    totalpl += int(rowone[1])
    amount = int(rowone[1])

    # Go thru Data
    for row in csvreader:
        date.append(row[0])

        change = (int(row[1])-amount)
        pl.append(change)
        amount = int(row[1])

        total_months += 1   

        totalpl = totalpl + int(row[1])

    
    mostincrease = max(pl)
    mostincreaselocation = pl.index(mostincrease)
    mostincreasedate = date[mostincreaselocation]


    mostdecrease = min(pl)
    mostdecreaselocation = pl.index(mostdecrease)
    mostdecreasedate = date[mostdecreaselocation]


    avgchange = sum(pl)/len(pl)
 
    # The net total amount of "Profit/Losses" over the entire period
    
    
    # The average of the changes in "Profit/Losses" over the entire period
    
    
    # The greatest increase in profits (date and amount) over the entire period

    
    # The greatest decrease in losses (date and amount) over the entire period

    
# Print Data

print (f'Financial Analysis')
print (f'___________________')
print (f'Total Months: ${total_months}')
print (f'Total: ${str(totalpl)}')
print (f'Average Change: ${str(round(avgchange,2))}')
print (f'Greatest Increase in Profit:  {mostincreasedate} (${str(mostincrease)})')
print (f'Greatest Decrease in Profits:  {mostdecreasedate}  (${str(mostdecreasedate)})')


# Set Variable for Output file
output_file = open("financialanalysis.txt", "w")

