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
    candidates = {}

#loop through list to count the total number of votes 
    for row in csvreader:
        votes_cast = votes_cast + 1 
    print(votes_cast)



    



#output_path = os.path.join('Analysis_Poll','Pypoll_results.txt')
#with open(output_path, 'w', newline ='') as txtfile: 