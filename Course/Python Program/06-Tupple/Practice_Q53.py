#Write a Python program to unzip a list of tuples into individual lists.
def unzip_tuples(tuple_list):
    # Use the zip() function with unpacking (*) to unzip
    return list(zip(*tuple_list))

# Example list of tuples
tuple_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Unzip the list of tuples
unzipped_lists = unzip_tuples(tuple_list)

# Display the results
for i, lst in enumerate(unzipped_lists, start=1):
    print(f"List {i}: {list(lst)}")
