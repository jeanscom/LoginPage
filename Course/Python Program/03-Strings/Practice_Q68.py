#Write a Python Program to Form a New String where the First Character and the Last Characters have been Exchanged.
def swap_first_last(input_string):
    # Check if the string has at least one character
    if len(input_string) < 2:
        return input_string  # No change if the string is empty or a single character
    
    # Swap the first and last characters
    new_string = input_string[-1] + input_string[1:-1] + input_string[0]
    return new_string

# Example usage
input_string = "hello"
result = swap_first_last(input_string)

print(f"Original string: {input_string}")
print(f"New string: {result}")
