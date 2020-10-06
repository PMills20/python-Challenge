import os 
import csv
filepath ="C:\\Users\\aptho\\Downloads\\Instructions\\Instructions\\PyBank\\Resources\\budget_data.csv"
#csvpath = os.path.join('PyBank','Resources','budget_data.csv')
profit_net=0
month=0
net_change_list=[]
net_change = 0
max_change = 0
min_change = 0
profit_increase = 0
profit_decrease = 0 

with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    first_row = next(csvreader)
    month = 1
    profit_net += int(first_row[1])
    prev_net =int(first_row[1])
    

    for row in csvreader:
        month += 1
        profit_net += int(row[1])
        net_change = int(row[1])- prev_net
        net_change_list += [net_change]

    avg_net_change = 0
    avg_net_change = int(net_change)/ len(net_change_list)
    
    
    max_change = max(net_change_list)
  
    
    
    min_change = min(net_change_list)
   
   
print("Financial Analysis") 
print("---------------------------------") 
print(f"Total Months: {month}") 
print(f"Total:  ${profit_net}") 
print(f"Average Change: {avg_net_change}") 
print(f"Greater Increase in Profits: {max_change}")
print(f"Greatest Descrease in Profits: {min_change}") 