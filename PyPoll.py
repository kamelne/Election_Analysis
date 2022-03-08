#The data we need to retrieve
# 1 The total number of votes cast
# 2 A complete list of canidates who received votes
# 3 The percentage of votes each canidata won
# 4 The total number of votes each canidate won
# 5 The winner of the electrion based on popular vote
# Open data file
# Retrieve all canidate names
# create vote count for each canidate 
# count votes per canidate
# get total vote count

import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")

file_to_save = os.path.join('analysis','election_analysis.txt')

with open(file_to_load) as election_data:

    # To do: perform analysis
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)
    print(election_data)
    headers = next(file_reader)
    print(headers)


with open(file_to_save,'w') as txt_file:

    txt_file.write("Counties in the Election\n"+ "-"*25 +"\nArapahoe\nDenver\nJefferson")
