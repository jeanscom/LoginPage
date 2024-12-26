# Write a Python program to print the calendar of a given month and year.
import calendar

# Read year and month from the user
year = int(input("Enter the year (e.g., 2023): "))
month = int(input("Enter the month (1-12): "))

# Display the calendar for the given month and year
print("\nHere is the calendar:")
print(calendar.month(year, month))
