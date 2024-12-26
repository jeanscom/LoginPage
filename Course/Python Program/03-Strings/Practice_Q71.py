#Write a Python function to insert a string in the middle of a string.
def insert_in_middle(original, insert):
    # Find the middle index of the original string
    mid_index = len(original) // 2
    
    # Insert the string in the middle
    new_string = original[:mid_index] + insert + original[mid_index:]
    
    return new_string

# Example usage
original_string = "HelloWorld"
insert_string = "Beautiful"
result = insert_in_middle(original_string, insert_string)

print(f"Original string: {original_string}")
print(f"New string: {result}")
