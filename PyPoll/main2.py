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

# Write variables 
    votes_cast = 0 
    candidate_list = []
    poll_results = {}

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
    Khan_percent = percent(Khan_votes,votes_cast)
    Correy_percent = percent(Correy_votes,votes_cast)
    Li_percent = percent(Li_votes,votes_cast)
    Otooley_percent = percent(Otooley_votes,votes_cast)
   
# state who the winner is 
    # make a little dictionary with members and total counts
    poll_results =[{"Candidate":"Khan",
                    "Votes":Khan_votes,
                    "Percent":Khan_percent}, 
                    {"Candidate":"Li","Votes": Li_votes , "Percent": Li_percent}, 
                    {"Candidate":"O'tooley",
                    "Votes":Otooley_votes,
                    "Percent":Otooley_percent}, 
                    {"Candidate":"Correy",
                    "Votes":Correy_votes,
                    "Percent":Correy_percent}]
    
    #Conditionals to find the winner through dictionary to see which had highest number of votes
    for results in poll_results:
        if Khan_votes > Li_votes and Otooley_votes and Correy_votes:
            winner = "Khan"
        elif Li_votes > Khan_votes and Otooley_votes and Correy_votes:
            winner = "Li"
        elif Otooley_votes > Khan_votes and Li_votes and Correy_votes: 
            winner = "O'tooley"
        else: 
            winner = "Correy"

# print results 
# Total number of votes 
print("Election results")
print("-----------------------------------------------------------")
print(f'Total votes: {votes_cast}')
print(f'Khan: {Khan_percent}  ({Khan_votes})')
print(f'Correy: {Correy_percent}  ({Correy_votes})')
print(f'Li: {Li_percent}  ({Li_votes})')
print(f'O´tooley: {Otooley_percent}  ({Otooley_votes})') # how to put ' without it interfering?
print("-----------------------------------------------------------")
print("Winner")
print("-----------------------------------------------------------")
print("Winner: "+ str(winner))


# prepare output file for results 
output_path = os.path.join('Analysis_Poll','Pypoll_results.txt')
with open(output_path, 'w', newline ='') as txtfile: 
    txtfile.writelines("-----------------------------------------------------\n")
    txtfile.writelines("Election results\n")
    txtfile.writelines("------------------------------------------------------\n")
    txtfile.writelines(f'Total votes: {votes_cast}\n')
    txtfile.writelines(f'Khan: {Khan_percent}  ({Khan_votes})\n')
    txtfile.writelines(f'Correy: {Correy_percent}  ({Correy_votes})\n')
    txtfile.writelines(f'Li: {Li_percent}  ({Li_votes})\n')
    txtfile.writelines(f'O´tooley: {Otooley_percent} ({Otooley_votes})\n') # how to put ' without it interfering?
    txtfile.writelines("-------------------------------------------------------\n")
    txtfile.writelines("Winner\n")
    txtfile.writelines("--------------------------------------------------------\n")
    txtfile.writelines("Winner: "+ str(winner))