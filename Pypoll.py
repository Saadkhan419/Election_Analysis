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
# total vote counter
total_votes = 0
# total number of candidates and votes.
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
        #to do: read and analyze the data here.
        # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        # Read the header row
        headers = next(file_reader)
        # Print each row in the CSV file.
        for row in file_reader:
#Add to the total vote count.
            total_votes +=1
#Print candidate name for each row
            candidate_name = row[2]
        #If the candidate does not match any existing candidate....
            if candidate_name not in candidate_options:            
                # Add it to the list of candidates.
                candidate_options.append(candidate_name)
                #Begin tracking that candidate's vote count
                candidate_votes[candidate_name] = 0
            #Add a vote to candidates count
            candidate_votes[candidate_name] += 1  
            #Save the results to our text file.
            #with open(file_to_save,"w") as txt_file:
    #Determine the percentage of votes for each candidate
    #1.Iterate through the candidate list.
for candidate_name in candidate_votes:
           # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
           # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
    print(f"{candidate_name} : {vote_percentage : .1f}% ({votes: ,})\n")
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
    if(votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    #  To do: print out the winning candidate, vote count and percentage
       
winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
print(winning_candidate_summary)
       