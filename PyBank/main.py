# Dependencies
import os
import csv

# Variables
months = []
profit_loss_changes = []

total_months = 0
net_total_pl = 0
original_month_pl = 0
current_month_pl = 0
profit_loss_change = 0


csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

        # Calculate total numbers of months included in the dataset
        total_months += 1

        # Calculate Net total amount of "Profit/Losses" over the entire period
        current_month_pl = int(row[1])
        net_total_pl += current_month_pl

        if (total_months == 1):
            original_month_pl = current_month_pl
            continue

        else:

            profit_loss_change = current_month_pl - original_month_pl
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            original_month_pl = current_month_pl

    # Calculate the average of the changes in "Profit/Losses" over the entire period
    sum_pl = sum(profit_loss_changes)
    avg_pl = round(sum_pl/(total_months - 1), 2)

    # Calculate the greatest increase in in profits (date and amount) over the entire period
    greatest_increase = max(profit_loss_changes)
    increase_index = profit_loss_changes.index(greatest_increase)
    best_month = months[increase_index]

    # Calculate the greatest decrease in in profits (date and amount) over the entire period
    greatest_decrease = min(profit_loss_changes)
    decrease_index = profit_loss_changes.index(greatest_decrease)
    worst_month = months[decrease_index]

    
    
    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_total_pl}")
print(f"Average Change:  ${avg_pl}")
print(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})")

output_path = os.path.join("Analysis","financial_analysis.txt")
with open(output_path, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-------------------\n")
    outfile.write(f"Total Months : {total_months}\n")
    outfile.write(f"Total: ${net_total_pl}\n")
    outfile.write(f"Average Change: ${avg_pl}\n")
    outfile.write(f"Greatest Increase in Profits: {best_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses: {worst_month} (${greatest_decrease}\n")