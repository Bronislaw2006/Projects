#TIP CALCULATOR

print("Welcome to tip calculator.")
bill = (float(input("what was the total bill? $")))
tip = (int(input("how much percent tip would you like to give to the waiter? 10, 12, 15?")))
person = (int(input("how many people to split the bill?")))
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill / person
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay : ${final_amount}")