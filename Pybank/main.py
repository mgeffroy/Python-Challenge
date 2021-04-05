#Pybank 

import os 
import csv 

# 1. Import csv file 

budget_csvpath = os.path.join('Resources_Pybank', 'Budget_data.csv')

with open(budget_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

# Say which is the header 
    csv_header = next (csvreader)
    print (f"CSV Header: {csv_header}")
# Create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset
        # 2.- Loop through everything to see which are the months 
        # The net total amount of "Profit/Losses" over the entire period
        # 4.- Add everything.
        # 5.- Print result 
    
    months = [] 
    profit = []
    month_count = 0 
    total_profit = 0
    for row in csvreader:
        month_count = month_count + 1
        total_profit = int(row[1]) + total_profit
    


    
    #print months 
    print (month_count)
    print(total_profit)

    
    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        # 6.- With previous answer divide everything by the lenght of list (or download average funcion of statistics module)
    # The greatest increase in profits (date and amount) over the entire period
        # 7.- Loop over every value on the list, 
        # 8.- Do one number minus the next one.
        # 9.- Find max of result ( use max.()) 
        # 10. Print both date and amount (first column) with the max result 
    # The greatest decrease in losses (date and amount) over the entire period
        # 11.- Loop over every value on the list
        #12.- Do one number minut the next one 
        # 13. Find min result (use min.())
        # 14. Print both date and amount with min result
    #Print the analysis in the terminal 
    #Export file into a text file 
