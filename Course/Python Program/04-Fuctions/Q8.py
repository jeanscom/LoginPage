# Function to check whether the mobile number is valid
def is_valid_mobile_number(number):
    # Check if the number has exactly 10 digits
    if len(number) == 10 and number.isdigit():
        # Check if the first digit is 7, 8, or 9
        if number[0] in ['7', '8', '9']:
            return True
        else:
            return False
    else:
        return False

# Main function to input and check the mobile number
def main():
    # Get input from the user
    mobile_number = input("Enter a mobile number: ")

    # Check if the mobile number is valid using the is_valid_mobile_number function
    if is_valid_mobile_number(mobile_number):
        print(f"{mobile_number} is a valid mobile number.")
    else:
        print(f"{mobile_number} is not a valid mobile number.")

# Call the main function
main()
