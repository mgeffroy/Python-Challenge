#Pybank homework 
#Import modules

import os 
import csv 
import statistics as stat

# Import csv file 

budget_csvpath = os.path.join('Resources_Pybank', 'Budget_data.csv')

with open(budget_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

# State that file has a header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
# Create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset
    
        # The net total amount of "Profit/Losses" over the entire period
        # 4.- Add everything.
     
   # Create variables for counting total months and start at zero
    month_count = 0 
    # Create variables for total profit and start at zero
    total_profit = 0
    # Create new list where information about changes in profit will be added 
    profit_diff = [] 

    #Create variables using next to be able to make the substraction for the change of profit list 
    
    Data_start = next(csvreader)
    Data_line2 = next(csvreader)

    #Create variable for difference
    diff = 0 

 # Loop through everything to see get the total sum of months and to get the total profit
    for row in csvreader:
        month_count = month_count + 1
        total_profit = int(row[1]) + total_profit
        diff = int(Data_start[1] - int(Data_line2[1]
        profit_diff.append(int(diff)
        #profit_diff = int(profit_sub - (row[1]))
        #change_profit.append(changes)
     
        
    

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        # 6.- With previous answer divide everything by the lenght of list (or download average funcion of statistics module)
    # The greatest increase in profits (date and amount) over the entire period
        # 7.- Loop over every value of the new list with the profit difference 
        # 8.- Do one number minus the next one.
        # 9.- Find max of result ( use max.()) 
        # 10. Print both date and amount (first column) with the max result 

        # 13. Find min result (use min.())
        # 14. Print both date and amount with min result
    
    # Print  information 
    print ("Financial Analysis")
    print ("----------------------------------------------------------------------")
    print ("Total months: " + str(month_count))
    print( "Total: $" + str (total_profit))

  #Export file into a text file 
#output_path = os.path.join('Analysis_Pybank','Pybank_results.txt')
#with open(output_path, 'w', newline ='') as txtfile:

    
     
  
