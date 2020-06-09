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

total_votes=0
candidate_options=[]
candidate_votes={}
candidate_percentage={}

county_list=[]
county_votes={}
county_percentage={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        total_votes  +=1
        
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 1
         
        else:
            candidate_votes[candidate_name]+=1         
        
        county_name=row[1]
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name]=1
          
        else:
            county_votes[county_name]+=1


# winning candidate list instad of string if we have more than one winner
winning_candidate = []
winning_percentage = 0

winning_count=max(candidate_votes.values())

for key,value in candidate_votes.items():
    if winning_count == value:
        winning_candidate.append(key)   
        winning_percentage=winning_count/total_votes*100

largest_county=[]

largest_count=max(county_votes.values())

for key,value in county_votes.items():
    if largest_count==value:
        largest_county.append(key)

with open(file_to_save, "w") as outfile:
    # Write some data to the file.

    outfile.write(
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    f"\nCounty Votes\n")


    for county, votes_county in county_votes.items():
        vote_percentage_county=(votes_county/total_votes)*100
        outfile.write(f"{county}: {vote_percentage_county:.1f}% ({votes_county})\n")
    
    outfile.write(
    f"\n-------------------------\n"
    f"Largest County: {','.join(largest_county)}\n"
    f"-------------------------\n")

    for name, votes in candidate_votes.items():
        vote_percentage=(votes/total_votes)*100
        outfile.write(f"{name}: {vote_percentage:.1f}% ({votes})\n")

    outfile.write(
    f"-------------------------\n"
    f"Winner: {','.join(winning_candidate)}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
print(total_votes)
print(candidate_percentage)
print(winning_candidate)
print(winning_count)
print(county_votes)
print(county_percentage)
print(largest_county)
    








