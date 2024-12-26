
# Summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his
# room cool. He has two options available:Rent a cooler at the cost of X coins per month.

# Purchase a cooler for Y coins. Given that the summer season will last for M months in
# Chefland, help Chef in finding whether he should rent the cooler or not. Chef rents the
# cooler only if the cost of renting the cooler is strictly less than the cost of purchasing it.
# Otherwise, he purchases the cooler.
# Print YES if Chef should rent the cooler, otherwise print NO

# Input number of test cases
T = int(input("Enter number of test cases: "))

# Process each test case
for _ in range(T):
    
     # Input: Renting cost per month (X), Purchase cost (Y), and the number of months (M)
    X, Y, M = map(int, input("Enter the renting cost per month (X), purchase cost (Y), and number of months (M): ").split())

# Calculate the total cost of renting for M months
    renting_cost = X * M

# Compare renting cost with the purchase cost
    if renting_cost < Y:
        print("YES")  # Rent the cooler if the renting cost is strictly less
    else:
        print("NO")  # Otherwise, purchase the cooler
