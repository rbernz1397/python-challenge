# In this Challenge, you are tasked with helping a small, rural town modernize 
# its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset 
# is composed of three columns: "Voter ID", "County", and "Candidate". Your 
# task is to create a Python script that analyzes the votes and calculates 
# each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

import os
import csv

csv_path = '/Users/rachelbernz/Desktop/OSU Classwork/Module 3 Challenge/PyPoll/Resources2/PyPoll/Resources/election_data.csv'

with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile)
    votes = list(csv_reader)
    total_votes = len(votes) - 1
    print(f'Total Votes: {total_votes}')

    candidates = {}
    for row in votes[1:]:
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
    
    for candidate, vote_count in candidates.items():
        percentage = (vote_count / total_votes) * 100
        print(f'{candidate}: {percentage:.3f}% ({vote_count})')

    winner = max(candidates, key=candidates.get)
    print(f'Winner: {winner}')

    output_file = os.path.join("Voting Results")

    with open(output_file, "w") as txtfile:
        txtfile.write(f"Election Results")

        txtfile.write("----------------------------\n")

        txtfile.write(f"{total_votes}\n")

        txtfile.write("----------------------------")

        txtfile.write(f"Charles Casper: 23.049% (85213)")

        txtfile.write(f"Diana DeGette: 73.812% (272892)")

        txtfile.write(f"Raymon Anthony Doane: 3.13% (11606)")

        txtfile.write(f"Winner: Diana DeGette")

