#Write a Python program to add a prefix text to all of the lines in a string
def add_prefix_to_lines(input_string, prefix):
    # Split the string into lines
    lines = input_string.split('\n')
    
    # Add the prefix to each line
    lines_with_prefix = [prefix + line for line in lines]
    
    # Join the lines back into a single string
    return '\n'.join(lines_with_prefix)

# Example usage
input_string = """Hello, world!
This is a test.
Python is awesome!"""
prefix = "Prefix: "

result = add_prefix_to_lines(input_string, prefix)

print("Original string:")
print(input_string)
print("\nString with prefix:")
print(result)
