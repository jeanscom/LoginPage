#Write a Python program to read and print various types of variables.
# Read an integer variable
int_var = int(input("Enter an integer: "))

# Read a floating-point variable
float_var = float(input("Enter a floating-point number: "))

# Read a string variable
string_var = input("Enter a string: ")

# Read a boolean variable (using 1/0 for True/False)
bool_var = bool(int(input("Enter 1 for True or 0 for False: ")))

# Print the variables and their types
print("\nYou entered the following variables:")
print(f"Integer: {int_var} (Type: {type(int_var)})")
print(f"Floating-point: {float_var} (Type: {type(float_var)})")
print(f"String: '{string_var}' (Type: {type(string_var)})")
print(f"Boolean: {bool_var} (Type: {type(bool_var)})")
