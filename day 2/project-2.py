'''
DAY 002 of 100
@author: Abhisek Ganguly
@topic: Project 2
'''
#Project: Tip calculator in Python.

bill = float(input("Enter then bill amount: $"))
people = int(input("How many ways do you want to split the bill? "))
tip = int(input("How much do you want to tip? (usually it's 15% to 20%) "))

f_bill = float(bill + (bill * (tip/100)))
f_bill_split = f_bill/people

print("Each person has to pay $", f_bill_split)