# Python Program to Convert Kilometres to Miles
# Conversion factor
KM_TO_MILES = 0.621371

# Input distance in kilometers
kilometers = float(input("Enter distance in kilometers: "))

# Convert kilometers to miles
miles = kilometers * KM_TO_MILES

# Display the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
