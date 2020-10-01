# Modules
import os
import csv
from collections import Counter

# Path to File
electionfile = os.path.join("Resources", "election_data.csv")

# Open the CSVFile
with open(electionfile) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip Header Row
    next(csvreader)

    electiondata = list(csvreader)

    totalvotes = len(electiondata)
    print (f'Total Votes: {totalvotes}')



print (f'Election Results')
print (f'___________________')
print (f'Total Votes: {totalvotes}')
print (f'___________________')



print (f'___________________')
print (f'Winner: ')
print (f'___________________')


# Set Variable for Output file
output_file = os.path.join("Analysis","Polling_Results.csv")

# Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Print in File
    writer.writerows()
