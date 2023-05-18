import csv
import os

# defineing the path to the csv file same as pybank method
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "election_data.csv")

candidates_votes = {}
total_votes = 0

# reading the csv file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates_votes:
            candidates_votes[candidate] = 0

        candidates_votes[candidate] += 1

winner = None
winner_votes = 0

# printing the analysis and store it in a list of strings
output = [
    "Election Results",
    "----------------------------",
    f"Total Votes: {total_votes}",
    "----------------------------",
]

print("\n".join(output))
