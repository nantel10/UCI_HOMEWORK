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

        # Tracking Dates
        date.append(row[0])


        # Calculate Changes
        change = (int(row[1])-amount)
        pl.append(change)
        amount = int(row[1])

        #Total Months
        total_months += 1   

        #Total Profit/Loss
        totalpl = totalpl + int(row[1])

    
    # Calulating Increases
    mostincrease = max(pl)
    mostincreaselocation = pl.index(mostincrease)
    mostincreasedate = date[mostincreaselocation]

    #Calulating Decreases
    mostdecrease = min(pl)
    mostdecreaselocation = pl.index(mostdecrease)
    mostdecreasedate = date[mostdecreaselocation]

    #Average of Changes in PL
    avgchange = sum(pl)/len(pl) 
    
# Print Data
print (f'Financial Analysis')
print (f'___________________')
print (f'Total Months: {total_months}')
print (f'Total: ${str(totalpl)}')
print (f'Average Change: ${str(round(avgchange,2))}')
print (f'Greatest Increase in Profit:  {mostincreasedate} (${str(mostincrease)})')
print (f'Greatest Decrease in Profits:  {mostdecreasedate}  (${str(mostdecreasedate)})')


# Set Variable for Output file
output_file = open("financialanalysis.txt", "w")

line1 = "Financial Analysis"
line2 = "___________________"
line3 = str(f'Total Months: {total_months}')
line4 = str(f'Total: ${str(totalpl)}')
line5 = str(f'Average Change: ${str(round(avgchange,2))}')
line6 =  (f'Greatest Increase in Profit:  {mostincreasedate} (${str(mostincrease)})')
line7 =  (f'Greatest Decrease in Profits:  {mostdecreasedate}  (${str(mostdecreasedate)})')

output_file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))