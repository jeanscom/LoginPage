#Write a Python program to count the total number of notes in a given amount    
# Input the amount from the user
amount = int(input("Enter the amount: "))

# Denominations available
notes = [100, 50, 20, 10, 5, 2, 1]

# Initialize a dictionary to store the number of notes of each denomination
note_count = {}

# Loop through each denomination
for note in notes:
    note_count[note] = amount // note  # Find the number of notes of this denomination
    amount = amount % note  # Update the amount with the remainder

# Print the result
print("Total number of notes:")
for note, count in note_count.items():
    if count > 0:
        print(f"{note} : {count} notes")
