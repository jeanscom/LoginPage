#Write a Python program to display the current date and time.
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format and display the current date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted_datetime)
