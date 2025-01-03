# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
cand_vote_percent = 0 # calculate the percentage of votes for each candidate


# Define lists and dictionaries to track candidate names and vote counts

# this list was not really used, but was very helpful in the development of the script, so I left it in here. 
list_candidate = ['test_candidate']

# The county list was never needed.
#list_county = ['test_county']

# this dictionary is not needed.
# dict_candidate_vote_count = {
#    # 'Name': 'test_name',
#    # 'Vote Count': '0'
# }   

# this "list of dictionaries" is used to store the vote counts for each candidate.  The commented structure of the dictionary is used for reference.
list_candidate_vote_count = [
   # {'Name': 'test_name', 'Vote Count': '0'}
]


# Winning Candidate and Winning Count Tracker
cand_most_votes = 0
cand_most_name = 'blank'

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        #set the vaiables to find unique to false
        found_candidate = False
        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes = int(total_votes) + 1

        # Get the candidate's name from the row
        candidate_name = row[2]


        # If the candidate is not already in the candidate list, add them
        while found_candidate == False:
            for i in range(len(list_candidate)):
                
                    if list_candidate[i] == row[2]:
                        #print(list_candidate[i])
                        #print(row[2])
                        found_candidate = True

                        # find the candidate in the dictionary list and update their vote count
                        for vc in range(len(list_candidate_vote_count)):
                             
                             #look to match the current name in the vote count dictionary and add a vote count
                             if list_candidate_vote_count[vc]['Name'] == row[2]:
                                list_candidate_vote_count[vc]['Vote Count'] = int(list_candidate_vote_count[vc]['Vote Count']) +1
                                #print(list_candidate_vote_count[vc]['Vote Count'])
                        
            # if the candidate is never found, append the name to the candidate list
            if found_candidate == False:

                #print("the list_candidate variable was not found")
                list_candidate.append(row[2])
                #I expected this to require an inital Vote Count value of 1, but that gave everyone an additional vote.
                list_candidate_vote_count.append({'Name':row[2],'Vote Count': str(0)})
    
        # Add a vote to the candidate's count
        # I dont do this here.  I do it above as I'm looping around the rows
    #print(list_candidate)
    #print(list_candidate_vote_count)

    # let's print to the terminal before we write to the file. (this ended up being down below as well.)
""" 
    print("Election Results")
    print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
    print(f"Total Votes: {"{:,}".format(total_votes)}")
    print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
    
    # loop through the Vote Count Dictionary List and print out the results for each one.
    for cand in range(len(list_candidate_vote_count)):
        # determine candidate's vote count and percentage
        cand_vote_percent = int(list_candidate_vote_count[cand]['Vote Count']) / int(total_votes)
        cand_vote_count = int(list_candidate_vote_count[cand]['Vote Count'])

        # find the candidate with the most votes and write the Name and percentage and total votes won
        if int(list_candidate_vote_count[cand]['Vote Count']) > cand_most_votes:
            cand_most_votes = int(list_candidate_vote_count[cand]['Vote Count'])
            cand_most_name = list_candidate_vote_count[cand]['Name']
        print(f"{list_candidate_vote_count[cand]['Name']}: {cand_vote_percent:.2%} ({cand_vote_count:,.0f})")
    
    # declare the winner
    print(f"Winner: {cand_most_name}") """
    
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results")
    print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
    print(f"Total Votes: {"{:,}".format(total_votes)}")
    print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")

    # Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")
    txt_file.write(f"Total Votes: {"{:,}".format(total_votes)}\n")
    txt_file.write(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for cand in range(len(list_candidate_vote_count)):

        # Get the vote count and calculate the percentage
        cand_vote_percent = int(list_candidate_vote_count[cand]['Vote Count']) / int(total_votes)
        cand_vote_count = int(list_candidate_vote_count[cand]['Vote Count'])

        # Update the winning candidate if this one has more votes
        if int(list_candidate_vote_count[cand]['Vote Count']) > cand_most_votes:
            cand_most_votes = int(list_candidate_vote_count[cand]['Vote Count'])
            cand_most_name = list_candidate_vote_count[cand]['Name']

        # Print and save each candidate's vote count and percentage
        print(f"{list_candidate_vote_count[cand]['Name']}: {cand_vote_percent:.2%} ({cand_vote_count:,.0f})")
        txt_file.write(f"{list_candidate_vote_count[cand]['Name']}: {cand_vote_percent:.2%} ({cand_vote_count:,.0f})\n")

    # Generate and print the winning candidate summary
    print(f"Winner: {cand_most_name}")

    # Save the winning candidate summary to the text file
    txt_file.write(f"Winner: {cand_most_name}\n")