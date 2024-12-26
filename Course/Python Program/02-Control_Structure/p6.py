
# You are building a program to calculate the cost of shipping a package. The cost depends on
# the weight of the package and the distance it needs to be shipped. Here are the rules:
# • If the package weighs less than or equal to 2 pounds, the base cost is $5.00.
# • If the package weighs more than 2 pounds but less than or equal to 10 pounds, the base
# cost is $10.00.
# • If the package weighs more than 10 pounds, the base cost is $20.00.
# • If the distance is less than or equal to 100 miles, there's no additional charge.
# • If the distance is greater than 100 miles but less than or equal to 500 miles, there's a
# $5.00 additional charge.
# • If the distance is greater than 500 miles, there's a $10.00 additional charge.
# # Input the weight of the package and the distance to be shipped
# weight = float(input("Enter the weight of the package (in pounds): "))
# distance = float(input("Enter the distance to be shipped (in miles): "))

# Determine the base cost based on weight
if weight <= 2:
    base_cost = 5.00
elif weight <= 10:
    base_cost = 10.00
else:
    base_cost = 20.00

# Determine the additional cost based on distance
if distance <= 100:
    additional_cost = 0.00
elif distance <= 500:
    additional_cost = 5.00
else:
    additional_cost = 10.00

# Calculate the total shipping cost
total_cost = base_cost + additional_cost

# Output the total shipping cost
print(f"The total shipping cost is: ${total_cost:.2f}")
