#Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3 then return the original string.
def get_first_three_chars(input_string):
    # Check if the string length is less than 3
    if len(input_string) < 3:
        return input_string
    # Otherwise, return the first three characters
    return input_string[:3]

# Example usage
input_string = "Hello"
result = get_first_three_chars(input_string)

print(f"Original string: {input_string}")
print(f"First three characters: {result}")
