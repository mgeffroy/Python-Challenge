#Pybank homework 
#Import modules

import os 
import csv 

# Import csv file 

budget_csvpath = os.path.join('Resources_Pybank', 'Budget_data.csv')

with open(budget_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

# State that file has a header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")    

   # Create variables for counting total months and start at zero
    month_count = 0 
    # Create variables for total profit and start at zero
    total_profit = 0
    # Create new list where information where changes in profit will be added 
    profit = []                     #List of profits
    profit_diff = []                #List of profit differences


 # Loop through everything to see get the total sum of months and to get the total profit
    for row in csvreader:
        month_count = month_count + 1
        total_profit = int(row[1]) + total_profit 
        # Add rows to profit list 
        profit.append(int((row[1])))
        
#Create variable profit difference by looping through profit list.   
    profit_diff = [profit[i + 1] - profit[i] for i in range(len(profit)-1)]
    
    # Calculate average of the differences between profits
      
    Average_change = round(sum(profit_diff)/ len(profit_diff),2)
   

    #Find max profit change and min profit change 
    max_value = max(profit_diff)
    min_value = min(profit_diff)

    # Find date (? depending on profit loss)
    
        # Print  information 
    print("Financial Analysis")
    print("----------------------------------------------------------------------")
    print("Total months: " + str(month_count))
    print( "Total: $" + str (total_profit))
    print(f'Average  Change: ${Average_change}')
    print(f'Greatest increase in profits: {max_value}')
    print(f'Greatest decrease in profits: {min_value}')

    # Export file into a text file 
    #Write everythin into text file
output_path = os.path.join('Analysis_Pybank','Pybank_results.txt')
with open(output_path, 'w', newline ='') as txtfile: 
    txtfile.write("Financial Analysis")
    txtfile.write("----------------------------------------------------------------------")
    txtfile.write("Total months: " + str(month_count))
    txtfile.write( "Total: $" + str (total_profit))
    txtfile.write(f'Average  Change: ${Average_change}')
    txtfile.write(f'Greatest increse in profits: {max_value}')
    txtfile.write(f'Greatest decrease in profits: {min_value}')
