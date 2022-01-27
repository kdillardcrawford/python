#Tip Calculator

print("Welcom to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))/100
people = int(input("How many people to split the bill? "))

total_tip = total*(1+tip)
each_person = round(total_tip/people, 2)

print(f"Each person should pay: ${each_person}.")