#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pybank

import os
import csv

# Open the file in read mode
pybank_csv = os.path.join(".", "Resources", "budget_data.csv")
#print(pybank_csv)

#set all the initial parameters
month_count = 0
net_total = 0
avg_change = []
avg_change_value = 0
value = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999999]

#open the file in read mode
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

#Skip the header
    csv_header = next(csvreader)    

#create a for loop to loop through the data and count the periods &  calculate required results
    for row in csvreader:
            # Count the number of rows
            month_count += 1
            
            # Calculate the Total
            net_total = int(row[1]) + net_total
            
            #Calculate average change
            avg_change_value = int(row[1]) - avg_change_value
            avg_change.append (avg_change_value)
            value.append(int(row[1]))
            
            #calculate Greatest increase and decrease in profits
            if avg_change_value > int(greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = avg_change_value
            elif int (row[1]) < int(greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = avg_change_value
             
            avg_change_value = int(row[1])
   

    avg_period = round((sum(avg_change[1:]) / (month_count - 1)), 2)

    # create the ouput format
output = (
        f"\nFinancial Analysis\n"
        f"----------------------\n"
        f"Total Months: {month_count}\n"
        f"Total: {net_total}\n"
        f"Average Change: {avg_period}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

#output the results in the txt file
output_pybank = os.path.join("Fin_Analysis_Results.txt")
with open (output_pybank, "w") as txt_file:
    txt_file.write(output)

# print results in terminal
print(output)


# In[ ]:





# In[ ]:





# In[ ]:




