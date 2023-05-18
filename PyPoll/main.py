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
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

output.extend([
    "----------------------------",
    f"Winner: {winner}",
    "----------------------------",
])

# defineing the path to the analysis file & writeing the analysis to a text file
analysis_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analysis", "analysis.txt")
with open(analysis_path, 'w') as textfile:
    textfile.write("\n".join(output))
