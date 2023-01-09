#Obtain the file 
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')

    total_months = 1
    total_profit = 0
    Headers = next (csvreader)
    second_row = next (csvreader)
    last_profit = second_row [1]
    start_profit = int(second_row [1])
    month_index = str(second_row[0])
    change = []
    date_index = []

    for row in csvreader :
        total_months = total_months + 1
        profit = int(row [1])
        total_profit = total_profit + (profit) 
        delta = profit - int(last_profit)
        last_profit = profit
        change.append(delta)
        date_index.append(row[0])
#output
total_change_profit = round(sum(change)/len(change))
max_change = max(change) 
min_change = min(change) 

max_change_index = change.index(max_change)
min_change_index = change.index(min_change)

max_date = date_index[max_change_index]
min_date = date_index[min_change_index]

print ("Total Months: " + str(total_months))
print ("Total Profit: " + "$" + str(total_profit + start_profit))
print ("Average Change: " + "$" + str(round(total_change_profit)))
print ("Greatest Increase in Profits: "+ str(max_date)+ " $" + str(max_change))
print ("Greatest Decrease in Profits: " + str(min_date)+ " $" + str(min_change))

#----Output file in txt
output_file = os.path.join("PyBank_results.txt") 

with open(output_file, "w") as datafile:
    print ("Financial Analysis",  file = datafile)
    print ("-------------------------------", file = datafile)
    print ("Total Months: " + str(total_months), file = datafile)
    print ("Total Profit: " + "$" + str(total_profit + start_profit), file = datafile)
    print ("Average Change: " + "$" + str(round(total_change_profit)),file = datafile)
    print ("Greatest Increase in Profits: "+ str(max_date)+ " $" + str(max_change), file = datafile)
    print ("Greatest Decrease in Profits: " + str(min_date)+ " $" + str(min_change), file = datafile)