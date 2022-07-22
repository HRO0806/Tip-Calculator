bill = input("What is the total on your bill?\n")
people = input("How many people are splitting the bill?\n")
tip = input("How much of a tip are you leaving(as a percentage)?\n")

def tip_calculator():
  bill_amount = float(bill)
  people_amount = float(people)
  tip_amount = float(tip)
  calculate = (bill_amount / people_amount) * (tip_amount / 100 + 1)
  print(round(calculate, 2))

tip_calculator()  