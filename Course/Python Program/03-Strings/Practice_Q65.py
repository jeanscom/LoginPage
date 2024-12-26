#write a Python Program to Replace all Occurrences of ‘a’ with ‘b’ in a String. If ‘a’ is not present then print the appropriate message.
def replace_a_with_b(input_string):
    # Check if 'a' is in the string
    if 'a' in input_string:
        # Replace all occurrences of 'a' with 'b'
        updated_string = input_string.replace('a', 'b')
        print("Updated string:", updated_string)
    else:
        print("The character 'a' is not present in the string.")

# Example usage
input_string = "apple and banana"
replace_a_with_b(input_string)

# Example with no 'a' in the string
input_string_no_a = "hello world"
replace_a_with_b(input_string_no_a)
