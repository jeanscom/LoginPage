# Write a program to count the occurrences of each character in a string using a dictionary.
# Input string
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character counts
ltr_count = {}

# Iterate through each character in the string
for i in input_string:
    # Increment the count if the character exists, else set it to 1
    if i in ltr_count:
        ltr_count[i] += 1
    else:
        ltr_count[i] = 1

# Print the character count dictionary
print("Character occurrences:", ltr_count)

