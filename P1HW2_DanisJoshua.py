# Caluclates and Determines Travel Cost 
# 9/26/22
# CTI-110 P1HW2 - Travel Expense
# Joshua Danis
#

print("This program calculates and displays travel expenses\n")

# prompt the user to enter the budget.
budget = float(input("Enter Budget: "))

# Prompt the user to enter the travel destination.
destination = input("\nEnter your travel destination: ")

# Prompt the user to enter the amount on gas.
gas = float(input("\nHow much do you think you will spend on gas? "))

# Prompt the user to enter the amount to be spend on lodging.
accomodation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))

# Then we prompt the user to enter the amount to be spend on food.
food = float(input("\nLast, how much do you need for food? "))

print("\n------------Travel Expenses------------")
# Next we print all the details.
print("Location:",destination)
print("Initial Budget:",budget)
print("\nFuel:",gas)
print("Accomodation:",accomodation)
print("Food:",food)

# We calculate the remaining balance by subtracting the gas, accomodation and food from the budget.
# The difference is stored in balance.
balance = budget - gas - accomodation - food


print("\nRemaining Balance:",balance)