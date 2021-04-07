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

# While coding got candidate list after first loop prepare vote count for each, starting at 0
    Khan_votes = 0  
    Otooley_votes = 0 
    Li_votes = 0
    Correy_votes = 0 

#loop through list to count the total number of votes 
    for row in csvreader:
        votes_cast = votes_cast + 1 
#Get names of different candidates putting them in a separate list and printing them
        candidate = str(row[2])
        if candidate not in candidate_list: 
            candidate_list.append(str(candidate))
     # Prepare conditional for adding votes obtained by each candidate
        if (candidate == 'Khan'):
           Khan_votes += 1
        elif(candidate == 'Correy'):
            Correy_votes = Correy_votes +1 
        elif (candidate == 'Li'):
            Li_votes = Li_votes + 1
        elif(candidate == "O'Tooley"):
            Otooley_votes +=1
      
    print(votes_cast)
    print(candidate_list)
    print(Khan_votes)
    print(Correy_votes)
    print(Li_votes)
    print(Otooley_votes)

#get percentages for votes of each candidate 
#Make percent function 
    def percent(n,m): 
        n=float(n)
        m=float(m)
        operation = round(((n * 100)/m),2)
        total = (f'{operation}%')
        return total
  #print percent for each candidate   
    print(percent(Khan_votes,votes_cast))
    print(percent(Correy_votes,votes_cast))
    print(percent(Li_votes,votes_cast))
    print(percent(Otooley_votes,votes_cast))
   
# Find winner 
    total_votes =[]
    total_votes = [Khan_votes,Otooley_votes,Correy_votes,Li_votes]
    winner = max(total_votes)
    print(winner)





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