# Tip Calculator<br><br>

This is a simple Tip Calculator built in Python that calculates how much each person should pay after splitting a bill, including a tip percentage provided by the user.<br>

**Table of Contents**<br>
- [Introduction](#introduction)<br>
- [Usage](#usage)<br>
- [Tip Calculation](#tip-calculation)<br>
- [Formula](#formula)<br>
- [Example](#example)<br><br>

**Introduction**<br>

This Python script helps users split a restaurant bill among multiple people while including a tip. The user can input the total bill amount, the percentage tip they wish to give, and the number of people to split the bill with. The script will calculate how much each person needs to pay.<br><br>

**Usage**<br><br>

1. Clone or download the project.<br>
2. Run the script using any Python environment or IDE.<br>
3. Follow the on-screen prompts:<br>
   - Enter the total bill amount.<br>
   - Enter the percentage of the tip you wish to give (e.g., 10%, 12%, 15%).<br>
   - Enter the number of people to split the bill.<br><br>

The script will calculate and display the amount each person should pay, including the tip.<br>

**How to Run**<br>

```bash
python tip_calculator.py




**EXAMPLE OUTPUT**


Welcome to tip calculator.

What was the total bill? $100

How much percent tip would you like to give? 10, 12, 15? 12

How many people to split the bill? 5

Each person should pay: $22.40


**FORMULA**


tip = (tip_percent / 100) * bill

total_bill = bill + tip

amount_per_person = total_bill / number_of_people


Where:

bill is the total bill amount in dollars.

tip_percent is the percentage of tip to be given (e.g., 10%, 12%, or 15%).

number_of_people is the number of people sharing the bill.


