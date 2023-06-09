import csv
import os

# csv file path(sruggled with the normal way had to resort to this)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "budget_data.csv")

months = []
profits = []


with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    
    header = next(csvreader)

    # store the months and profits in lists
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

# defineing a list to store the changes in profits
profit_changes = []

# calculate the changes in profits greatest increase and decrease in profits
for i in range(1, len(profits)):
    profit_changes.append(profits[i] - profits[i - 1])

greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# finding the months corresponding to the greatest increase and decrease
greatest_increase_month = months[profit_changes.index(greatest_increase) + 1]
greatest_decrease_month = months[profit_changes.index(greatest_decrease) + 1]

# calculating the total number of months, the net total of profits, and the average change in profits
total_months = len(months)
net_total = sum(profits)
average_change = sum(profit_changes) / len(profit_changes)

# printing the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


analysis_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analysis", "analysis.txt")

# writing the analysis to a text file opening and closing
with open(analysis_path, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
