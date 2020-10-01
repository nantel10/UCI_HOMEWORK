# Modules
import os
import csv


# Path to File
electionfile = os.path.join("Resources", "election_data.csv")

canditates = []

votescount = []

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
            votescount.append(1)
        else:
            counter = canditates.index(row[2])
            votescount[counter] += 1

    for votes in votescount:
        percent = (votes/totalvotes) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        votepercent.append (percent)
    
    winnercalc = max(votescount)
    index = votescount.index(winnercalc)
    winner = canditates[index]

# Print Results
print (f'Election Results')
print (f'___________________')
print (f'Total Votes: {str(totalvotes)}')
print (f'___________________')
for x in range(len(canditates)):
    print(f'{canditates[x]}:  {str(votepercent[x])}  {str(votescount[x])}')
print (f'___________________')
print (f'Winner:  {winner}')
print (f'___________________')


# Export Txt
output_file = open("Polling_Results.txt", "w")
line1 = 'Election Results'
line2 = '___________________'
line3 = str(f'Total Votes: {str(totalvotes)}')
line4 = str(f'___________________')
output_file.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for x in range(len(canditates)):
    line = str(f'{canditates[x]}:  {str(votepercent[x])}  {str(votescount[x])}')
    output_file.write('{}\n'.format(line))
line5 = '___________________'
line6 = str(f'Winner:  {winner}')
line7 = '___________________'
output_file.write('{}\n{}\n{}\n'.format(line5, line6, line7))
