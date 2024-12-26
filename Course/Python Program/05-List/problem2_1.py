# Take a list as user input, without using inbuilt function, Edit the list by deleting an element from a position pos. Print the new list

# Step 1: Take user input for the list
input_list = input("Enter the elements of the list separated by spaces: ")

# Step 2: Convert the input into a list without using built-in functions
my_list = []
current_element = ""
for char in input_list:
    if char == " ":
        if current_element:  # Avoid adding empty strings
            my_list.append(current_element)
            current_element = ""
    else:
        current_element += char
if current_element:  # Add the last element if exists
    my_list.append(current_element)

# Step 3: Take user input for the position to delete
pos = int(input("Enter the position of the element to delete (0-based index): "))

# Step 4: Delete the element at the specified position
new_list = []
for i in range(len(my_list)):
    if i != pos:  # Skip the element at the specified position
        new_list.append(my_list[i])

# Step 5: Print the modified list
print("New list after deletion:", new_list)