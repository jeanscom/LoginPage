
# Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the
# assignments at X pm. Each assignment takes him 1 hour to complete. Can you tell
# whether he'll be able to complete all assignments on time or not?

# Input number of test cases
T = int(input("Enter number of test cases: "))

# Process each test case
for _ in range(T):
    
   # Input: Starting time in pm (X)
    X = int(input("Enter the starting time in pm (X): "))

# Check if he can complete all assignments before 10 pm
    if X + 3 <= 10:
        print("Yes")
    else:
        print("No")

