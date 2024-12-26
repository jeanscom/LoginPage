
# Input number of test cases
T = int(input("Enter number of test cases: "))

# Process each test case
for _ in range(T):
    
    # Input: cost of double room (x) and triple room (y)
    x, y = map(int, input("Enter the cost of a double room (x) and a triple room (y): ").split())

# Option 1: 3 double rooms
    cost_option1 = 3 * x

# Option 2: 2 triple rooms
    cost_option2 = 2 * y

# Option 3: 1 double room + 1 triple room
    cost_option3 = x + y

# Find the minimum cost
    min_cost = min(cost_option1, cost_option2, cost_option3)

# Output the minimum cost
    print(f"The minimum cost to accommodate 6 people is: {min_cost}")

