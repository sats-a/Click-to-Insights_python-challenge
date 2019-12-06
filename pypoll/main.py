#!/usr/bin/env python
# coding: utf-8

# In[11]:


#pypoll

#importing the dependencies
import os
import csv

#file to read and output

file_to_read = os.path.join(".", "Resources", "election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

#total vote counter
total_votes = 0

#candidate option and vote counter
candidate_option = []
candidate_votes = { }

#winning candidate and winning count tracker
winning_canidate = ""
winning_count = 0

#Read csv

with open(file_to_read, newline="") as election_data:
    reader = csv.reader(election_data, delimiter=",")
    
#read the header

    header = next(reader)
    
    for row in reader:
        
        #calculate total vote count
        total_votes = total_votes + 1
        
        #extract candidate name from each row
        candidate_name = row[2]
        
        #if the candidate does not match any existing candidate
        
        if candidate_name not in candidate_option:
            #add it to the list of candidates in the running
            candidate_option.append(candidate_name)
            
            #begin tracking that candidate, votes count start at 0
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        output = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------\n"
        )

print(output)

#open the file to write
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
    
#determine the candidate by looping through the counts

    for candidate in candidate_votes:
        
        #retrieve votes count and percentages
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes) / float(total_votes) * 100
        
        #determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        #print each candidate voters count and percentage
        voter_output = f"{candidate}: {votes_percentage:.3f}% ({votes})\n"
        
        print (voter_output, end="")
        txt_file.write(voter_output)
    
    
    # the winning candidates
    
    winning_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------\n"
    )
    print(winning_summary)
    
    #save the winning candidate to txt file
    
    txt_file.write(winning_summary)


# In[ ]:




