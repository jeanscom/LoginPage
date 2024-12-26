
# You are tasked with writing a Python program that calculates income tax for individuals
# based on their income and tax brackets. Your program should follow these rules:
# The tax calculation is based on the following tax brackets:
# • Up to $10,000: 5% tax
# • $10,001 to $50,000: 10% tax
# • $50,001 to $100,000: 20% tax
# • Over $100,000: 30% tax
# There is also an additional tax deduction of $500 for individuals over 65 years old. If an
# individual has children, they receive a tax credit of $200 for each child. Write a Python
# program that takes input for an individual's income, age, and the number of children
# and calculates their income tax.

# Input: Income, Age, and Number of children
income = float(input("Enter your income: "))
age = int(input("Enter your age: "))
children = int(input("Enter the number of children: "))

# Calculate the tax based on income
if income <= 10000:
    tax = income * 0.05
elif income <= 50000:
    tax = 10000 * 0.05 + (income - 10000) * 0.10
elif income <= 100000:
    tax = 10000 * 0.05 + 40000 * 0.10 + (income - 50000) * 0.20
else:
    tax = 10000 * 0.05 + 40000 * 0.10 + 50000 * 0.20 + (income - 100000) * 0.30

# Apply the age deduction if over 65
if age > 65:
    tax -= 500  # Tax deduction for individuals over 65

# Apply the tax credit for children
tax_credit = children * 200
tax -= tax_credit  # Deduct the tax credit for children

# Ensure tax is not negative
if tax < 0:
    tax = 0

# Output the calculated tax
print(f"Your calculated income tax is: ${tax:.2f}")
