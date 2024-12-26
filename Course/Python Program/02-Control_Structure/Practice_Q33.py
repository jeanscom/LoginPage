#Write a Python program to find the frequency of each digit in a given integer.
# Input a number from the user
num = int(input("Enter a number: "))

# Convert the number to a string to easily iterate over its digits
num_str = str(num)

# Initialize a dictionary to store the frequency of each digit
digit_frequency = {}

# Loop through each digit in the number
for digit in num_str:
    if digit in digit_frequency:
        digit_frequency[digit] += 1  # Increment the count if the digit is already in the dictionary
    else:
        digit_frequency[digit] = 1  # Add the digit to the dictionary with a count of 1

# Print the frequency of each digit
print("Frequency of each digit:")
for digit, count in digit_frequency.items():
    print(f"{digit}: {count}")
