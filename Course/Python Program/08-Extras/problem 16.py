
# Vaidehi has two pet dogs, a Golden Retriever and a Great Dane. As per their nature, Golden Retriever is full of energy and wants to play around while Great Dane is not a huge fan of exercise. Vaidehi knows that a Golden Retriever without exercise engages in destructive behaviour, but she cannot leave Great Dane alone. So, she takes them for exercise every morning. While the Golden Retriever trots X meters per minute, the Great Dane walks Y meters per minute, such that (Y < X). Given that the exercise time is N minutes, How many meters would each dog cover? 

 
X = int(input("Enter the speed of the Golden Retriever (meters per minute): "))
Y = int(input("Enter the speed of the Great Dane (meters per minute): "))
N = int(input("Enter the exercise time (in minutes): "))

if X <= 0 or Y <= 0 or N <= 0:
    print("Please enter positive values for speeds and time.")
elif Y >= X:
    print("The speed of the Great Dane should be less than the Golden Retriever.")
else:
    # Calculate distances without using *
    golden_distance = 0
    for _ in range(N):
        golden_distance += X

    great_dane_distance = 0
    for _ in range(N):
        great_dane_distance += Y

    print(f"The Golden Retriever covers {golden_distance} meters.")
    print(f"The Great Dane covers {great_dane_distance} meters.")
