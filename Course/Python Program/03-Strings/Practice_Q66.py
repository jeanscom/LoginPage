#Write a Python Program to Remove the nth Index Character from a Non-Empty String
def remove_nth_char(input_string, n):
    # Check if n is a valid index
    if n < 0 or n >= len(input_string):
        print("Invalid index.")
        return input_string
    
    # Remove the character at the nth index
    updated_string = input_string[:n] + input_string[n+1:]
    return updated_string

# Example usage
input_string = "Hello, World!"
n = 7
result = remove_nth_char(input_string, n)

print(f"Original string: {input_string}")
print(f"Updated string: {result}")
