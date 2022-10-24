from tkinter import N
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Question 1. With a for & while loop, print even numbers from 1 - 30.
# For loop
print("Answer to question 1: \n")
for x in range(1, 32):
    if (x % 2 == 0):
        print(f"{Fore.GREEN} {x} is an even number in this \'for loop\'")
print("======================================")
# While Loop
number = 1
while number <= 30:
    if (number % 2 == 0):
        print(f"{Fore.RED} {number} is an even number in this while loop")
    number += 1

# Question 2. With a for & while loop, print odd numbers from 1 - 30.
# For Loop
print("====================================== \n")
print("Answer to question 2: \n")
for x in range(1, 30):
    if (x % 2 != 0):
        print(f" {Fore.GREEN} {x} is an odd number in this \'for loop\'")
print("======================================")
# While Loop
number = 1
while number <= 30:
    if (number % 2 != 0):
        print(f"{number} is an odd number in this while loop")
    number += 1
print("======================================")
# Question 3: Ahmed, an EiT Fellow, has been given an amount of GHC 50,000 for his capstone project.
# 25% of this amount was spent on marketing,
# 50% was spent on other operational expenses,
# The remaining 25% on customer acquisition,
# It will cost him GHC 5 to acquire a customer
# Task:
# Write a python program to prepare his financial statement
# Your program should calculate the number of customers he can acquire with the budget allocated
print("Answer to question 3: \n")
print(f"{Fore.RED}Mr Ahmed's Financial Statement (October 1 - October 31 2022)")
stipend = input("Enter Capstone Stipend: ")
capstone_stipend = int(stipend)
#
marketing_expenditure = 0.25 * capstone_stipend
fb_ads = 0.1*capstone_stipend
google_ads = 0.1*capstone_stipend
TikTok_ads = 0.05*capstone_stipend
#
operational_expenditure = 0.5 * capstone_stipend
a4_paper = 0.05*capstone_stipend
printing_costs = 0.05*capstone_stipend
Transportation = 0.1*capstone_stipend
airtime = 0.05*capstone_stipend
#
cac = 0.25 * capstone_stipend
can_aquire_customers = int(cac/5)
#
balance = capstone_stipend - \
    (marketing_expenditure + operational_expenditure + cac)

print(f"{Back.GREEN}Total Capstone budget Allocated: GHC {capstone_stipend}")
print("======================================")
print("Expenditure Log")
print("======================================")
print(f"{Back.RED}Total Capstone Marketing Expenses: GHC {marketing_expenditure}")
print("Marketing Expense breakdown by Channel:")
print(f" Facebook Ads: GHC {fb_ads}")
print(f" Google Ads: GHC {google_ads}")
print(f" TikTok Ads: GHC {TikTok_ads}")
print("======================================")
print(f"{Back.RED}Total Capstone Operational Expenses: GHC {operational_expenditure}")
print(" Operational Expenses breakdown :")
print(f"  Purchase of a4 Paper: GHC {a4_paper}")
print(f"  Cost of printing: GHC {printing_costs}")
print(f"  Transport Expenses: GHC {Transportation}")
print(f"  Airtime and communication: GHC {airtime}")
print("======================================")
print(f"{Back.RED}Total Customer Aquisition Expenses: GHC {cac}")
print("  Unit customer acquisition cost : GHC 5.00")
print(f"  Total Number of customers Acquired : {can_aquire_customers}")
print("======================================")
print(f"{Back.RED}Balance after Expenses = GHC {balance}")
