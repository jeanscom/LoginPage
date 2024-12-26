# Write a Python program to convert a given string into a list of words.
def string_to_word_list(input_string):
    # Split the string into words using whitespace as the delimiter
    word_list = input_string.split()
    return word_list

# Example usage
input_string = "Python is an amazing programming language"
result = string_to_word_list(input_string)

print(f"Original string: {input_string}")
print(f"List of words: {result}")
