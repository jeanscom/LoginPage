
# Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob. Right now, Limak and Bob weigh a and b respectively. It's guaranteed that Limak's weight is smaller than or equal to his brother's weight. Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year. After how many full years will Limak become strictly larger (strictly heavier) than Bob?

 # Input the weights of Limak and Bob
a = int(input("Enter Limak's weight: "))
b = int(input("Enter Bob's weight: "))

# Initialize the number of years
years = 0

# Continue the process until Limak's weight exceeds Bob's weight
while a <= b:
    a *= 3  # Limak's weight triples
    b *= 2  # Bob's weight doubles
    years += 1  # Increment the year count

# Output the number of years
print(f"Limak will become strictly heavier than Bob after {years} years.")
