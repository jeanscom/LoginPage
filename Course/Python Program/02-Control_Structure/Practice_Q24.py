#Write a Python program to input the week number and print the weekday.
# Input the week number from the user
week_num = int(input("Enter the week number (1-7): "))

# Check the week number and print the corresponding weekday
if week_num == 1:
    print("Monday")
elif week_num == 2:
    print("Tuesday")
elif week_num == 3:
    print("Wednesday")
elif week_num == 4:
    print("Thursday")
elif week_num == 5:
    print("Friday")
elif week_num == 6:
    print("Saturday")
elif week_num == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
