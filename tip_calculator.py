print("Welcome to the tip calculator!")
#bill total
bill = float(input("What was the total bill?\n $"))
#tip amount
tip = int(input("How much tip would you like to give? Exp. 10, 15?\n "))
#How many peoply are you splitting the bill with?
split = int(input("How many people to split the bill?\n "))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split
final_sum = round(bill_per_person, 2)
total = (f"Each person should pay: ${final_sum}")
print(total)

