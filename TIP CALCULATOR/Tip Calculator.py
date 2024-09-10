# Tip Calculator

# Print a welcome message to the user.
print("Welcome to tip calculator.")

# Ask the user for the total bill amount, convert the input to a float, and store it in the 'bill' variable.
bill = float(input("What was the total bill? $"))

# Ask the user what percentage tip they would like to give, convert the input to an integer, and store it in 'tip'.
tip = int(input("How much percent tip would you like to give? 10, 12, 15? "))

# Ask the user how many people will split the bill, convert the input to an integer, and store it in 'person'.
person = int(input("How many people to split the bill? "))

# Convert the tip percentage to a decimal by dividing it by 100, and store it in 'tip_as_percent'.
tip_as_percent = tip / 100

# Calculate the total tip amount by multiplying the bill by the tip percentage.
total_tip = bill * tip_as_percent

# Calculate the total bill amount (bill + tip) and store it in 'total_bill'.
total_bill = bill + total_tip

# Divide the total bill by the number of people to get the amount each person needs to pay.
bill_per_person = total_bill / person

# Round the final amount each person should pay to 2 decimal places.
final_amount = round(bill_per_person, 2)

# Format the final amount to ensure it has exactly two decimal places and store it as a string.
final_amount = "{:.2f}".format(bill_per_person)

# Print the amount each person should pay.
print(f"Each person should pay: ${final_amount}")
