#Write a Python program to get the last part of a string before a specified character
def get_last_part_before_char(input_string, char):
    # Find the index of the specified character
    index = input_string.rfind(char)
    
    # If the character is found, return the part before it
    if index != -1:
        return input_string[:index]
    else:
        # If the character is not found, return the original string
        return input_string

# Example usage
input_string = "example@domain.com"
char = "@"
result = get_last_part_before_char(input_string, char)

print(f"Original string: {input_string}")
print(f"Last part before '{char}': {result}")
