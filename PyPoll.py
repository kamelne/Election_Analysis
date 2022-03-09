#The data we need to retrieve
# 1 The total number of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each canidata won
# 4 The total number of votes each candidate won
# 5 The winner of the electrion based on popular vote
# Open data file
# Retrieve all candidate names
# create vote count for each candidate 
# count votes per candidate
# get total vote count

import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")

file_to_save = os.path.join('analysis','election_analysis.txt')

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    # To do: perform analysis
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes))*100
        formatted_percentage= "{:.1f}".format(vote_percentage)
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


winning_candidate_summary = (
    "--------------------------------\n"
    f"Winner: {winning_candidate} \n"
    f"Winning Vote Count:  {winning_count:,} \n"
    f"Winning Percentage: {winning_percentage:.1f}% \n"
    "--------------------------------\n"
)

print(winning_candidate_summary)
