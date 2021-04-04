#Pybank 

import os 
import csv 

# 1. Import csv file 

csvpath = os.path.join('..', 'Resources_Pybank', 'Budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

# Say which is the header 
# 
# Create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset
        # 2.- Loop through everything to see which are the months 
        # 3.- Print months 
    # The net total amount of "Profit/Losses" over the entire period
        # 4.- Add everything.
        # 5.- Print result 

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