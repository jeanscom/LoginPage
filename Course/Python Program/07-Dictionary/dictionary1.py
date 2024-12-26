# Write a program to check if the key 'city' exists in a dictionary. If it exists, print its value; otherwise, print "Key not found".
# Sample dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Check if the key 'city' exists
if 'city' in my_dict:
    print("Value of 'city':", my_dict['city'])
else:
    print("Key not found")
    