# tip_calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip: int = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = (tip/100 +1)
tip_given = (bill * tip)/people
print(round(tip_given , 2))
