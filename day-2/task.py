print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? ") or "0")
number_of_people = int(input("How many people to split the bill? "))
total_tip = bill / 100 * tip_percentage
total_bill = bill + total_tip
result = total_bill / number_of_people

print(f"Each person should pay: ${round(result, 2)}")
