# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources", "election_analysis.txt")

# Initialize a total vote counter
total_votes=0

# list of candidates who received votes
candidate_options=[]

# dictionary: Key:candidate name, value:number of votes each candidate won
candidate_votes={}

# dictionary: Key:candidate name, value:percentage of votes each candidate won
candidate_percentage={}

county_list=[]

# dictionary: Key:county name, value:number of votes in each county
county_votes={}

# dictionary: Key:county name, value:percentage of total votes
county_percentage={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    for row in file_reader:
        total_votes  +=1
        
        # A complete list of candidates who received votes
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 1
         
        else:
            candidate_votes[candidate_name]+=1         
        
        # A complete list of counties in election
        county_name=row[1]
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name]=1
          
        else:
            county_votes[county_name]+=1


# winning candidate list instad of string in case we have more than one winner
winning_candidate = []

# calculation for the winner of the election, name, number of votes, percentage of votes
winning_count=max(candidate_votes.values())

for key,value in candidate_votes.items():
    if winning_count == value:
        winning_candidate.append(key)   
        winning_percentage=winning_count/total_votes*100

# winning county list instad of string in case we have more than one county has the highest number of votes
largest_county=[]

# calculation for largest county in the election, print to terminal and a text file
largest_count=max(county_votes.values())

for key,value in county_votes.items():
    if largest_count==value:
        largest_county.append(key)

with open(file_to_save, "w") as outfile:

    outfile.write(
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    f"\nCounty Votes\n")
    print(f"\nTotal Votes: {total_votes:,}\n"
    f"-------------------------\n")

    # percentage calculation for each county and printing the vote count and percentage to terminal and a text file
    for county, votes_county in county_votes.items():
        vote_percentage_county=(votes_county/total_votes)*100
        outfile.write(f"{county}: {vote_percentage_county:.1f}% ({votes_county:,})\n")
        print(f"{county}: {vote_percentage_county:.1f}% ({votes_county:,})\n")

    outfile.write(
    f"\n-------------------------\n"
    f"Largest County: {','.join(largest_county)}\n"
    f"-------------------------\n")
    print(f"\n-------------------------\n"
    f"Largest County: {','.join(largest_county)}\n"
    f"-------------------------\n")

     # percentage calculation for each candidate and printing the vote count and percentage to terminal and a text file
    for name, votes in candidate_votes.items():
        vote_percentage=(votes/total_votes)*100
        outfile.write(f"{name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(f"{name}: {vote_percentage:.1f}% ({votes:,})\n")

    outfile.write(
    f"-------------------------\n"
    f"Winner: {','.join(winning_candidate)}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
    print(f"-------------------------\n"
    f"Winner: {','.join(winning_candidate)}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    








