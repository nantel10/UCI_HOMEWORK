# Modules
import os
import csv


# Path to File
electionfile = os.path.join("Resources", "election_data.csv")

canditates = []

candidatesvote = []

votepercent = []

totalvotes = 0


# Open the CSVFile
with open(electionfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip Header Row
    csv_header = next(csvreader)

    for row in csvreader:
        totalvotes += 1
    
        if row[2] not in canditates:
            canditates.append(row[2])
            counter = canditates.index(row[2])
            totalvotes.append(1)
        else:
            counter = canditates.index(row[2])
            totalvotes[counter] += 1

    for votes in totalvotes:
        percent = (votes/totalvotes) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        votepercent.append (percent)

    




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
