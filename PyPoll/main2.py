#PyPoll homework 
# To do: 
#The total number of votes cast
# A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#Plan 
#import modules 
import os 
import csv 

#Direction  to file 
poll_csvpath = os.path.join('Resources_Poll','Poll_data.csv')

# Read the file 
with open(poll_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

# State that file has a header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 

# Write variables 
    votes_cast = 0 
    candidate_list = []


#loop through list to count the total number of votes 
    for row in csvreader:
        votes_cast = votes_cast + 1 
        candidate = str(row[2])
        if candidate not in candidate_list: 
            candidate_list.append(str(candidate))
    print(votes_cast)
    print(candidate_list)
#After getting candidate list prepare vote count for each
    Khan_votes = 0 
    Li_votes = 0 
    Otooley_votes = 0 
    Correy_votes = 0 
# Prepare conditional for adding votes obtained by each candidate

    for row in csvreader:
       if row[2] == "Khan":
           Khan_votes += 1
    print(Khan_votes)
        #elif row[1] == "Li":
           #Li_votes += "Li"

#get percentages for votes of each candidate 
# state who the winner is 
    # make a little dictionary with members and total counts
    #loop through dictionary to see which had highest number of votes

# print results 
# Total number of votes 
#("Election results")
#("-----------")
#()

# prepare output file for results 
#output_path = os.path.join('Analysis_Poll','Pypoll_results.txt')
#with open(output_path, 'w', newline ='') as txtfile: 