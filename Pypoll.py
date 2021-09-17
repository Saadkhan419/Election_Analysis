# The data we need to retrieve.
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
file_to_load = 'Resources\election_results.csv'
# Open the election results and read
with open(file_to_load, encoding='utf-8') as election_data:
    # to do: perform analysis
    print(election_data)
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
        #to do: read and analyze the data here.
        # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        # Print the header row
        headers = next(file_reader)
        print(headers)