# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

#get current working directory to make sure the files are present
print(os.getcwd())


# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
total_value = 0
largest_loss = 0
largest_loss_month = "Today"
largest_gain = 0
largest_gain_month = "Today"
average_change = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    print(f"CSV Header: {header}")

    # Track the total and net change
    first_data = next(reader)
    total_value = first_data[1]
    total_months = total_months + 1

    # Process each row of data
    # I did not expect to have to cast each veriable as an integer for all the calculations.
    for row in reader:
    
        #count the months
        total_months = total_months + 1    

        # Track the total
        total_value = int(total_value) + int(row[1])

        # Track the net change
        total_net = int(total_net) + int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if int(row[1]) > largest_gain:
            largest_gain = int(row[1])
            largest_gain_month = row[0]


        # Calculate the greatest decrease in losses (month and amount)
        if int(row[1]) < largest_loss:
            largest_loss = int(row[1])
            largest_loss_month = row[0]

# Calculate the average net change across the months
# the changes happen over one less month than the total months
average_change = total_net / (total_months - 1)


# Generate the output summary


# Print the output
print(f"Financial Analysis")
print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
print(f"Total Months: {total_months}")
print(f"Total Ending Value: {"${:,.2f}".format(total_value)}")
#print(f"Total Change: {"${:,.2f}".format(total_net)}")
print(f"Average Change: {"${:,.2f}".format(average_change)}")
print(f"Greatest Profit (Month / Amount): {largest_gain_month} / {"${:,.2f}".format(largest_gain)}")
print(f"Lowest Profit (Month / Amount): {largest_loss_month} / {"${:,.2f}".format(largest_loss)}")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
#    txt_file.write(output)
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total Ending Value: {"${:,.2f}".format(total_value)}\n")
    #txt_file.write(f"Total Change: {"${:,.2f}".format(total_net)}\n")
    txt_file.write(f"Average Change: {"${:,.2f}".format(average_change)}\n")
    txt_file.write(f"Greatest Profit (Month / Amount): {largest_gain_month} / {"${:,.2f}".format(largest_gain)}\n")
    txt_file.write(f"Lowest Profit (Month / Amount): {largest_loss_month} / {"${:,.2f}".format(largest_loss)}\n")