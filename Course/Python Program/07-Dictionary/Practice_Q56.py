# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
def highest_three_values(input_dict):
    # Sort the dictionary items by value in descending order and select the top 3
    return sorted(input_dict.items(), key=lambda x: x[1], reverse=True)[:3]

# Example dictionary
sample_dict = {'a': 50, 'b': 20, 'c': 80, 'd': 60, 'e': 40}

# Find the highest 3 values
top_3 = highest_three_values(sample_dict)

# Display the result
print("Original dictionary:", sample_dict)
print("Top 3 highest values with keys:", top_3)
