#In this Challenge, you are tasked with creating a Python script to analyze the
#financial records of your company. You will be given a financial dataset called
#budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

#Your task is to create a Python script that analyzes the records to calculate
#each of the following values:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period


import os
import csv


csv_path = '/Users/rachelbernz/Desktop/OSU Classwork/Module 3 Challenge/PyBank/Resources/PyBank/Resources/budget_data.csv'

total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",10]

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    for row in csv_reader:
        total_months += 1
        total_profit_loss = int(row[1])
        profit_loss_change = int(row[1]) - prev_profit_loss
        prev_profit_loss = int(row[1])

        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change
        
        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

        average_change = round(total_profit_loss/total_months,2)
    
    print("Financial Analysis")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Avereage Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})")    


output_file = os.path.join("analysis_for_budget_analysis.txt")

with open(output_file, "w") as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    
    txtfile.write(f"Average Change: ${average_change}\n")

    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")

    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

