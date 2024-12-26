# Petya is having a party soon, and he has decided to invite his n friends.

# He wants to make invitations in the form of origami. For each invitation, he needs two red sheets, five green sheets, and eight blue sheets. The store sells an infinite number of notebooks of each color, but each notebook consists of only one color with k sheets. That is, each notebook contains k sheets of either red, green, or blue.

# Find the minimum number of notebooks that Petya needs to buy to invite all n of his friends.
# Input: number of friends and number of sheets per notebook
n = int(input("Enter the number of friends: "))
k = int(input("Enter the number of sheets per notebook: "))

# Total sheets required for n friends
total_red_sheets = n * 2
total_green_sheets = n * 5
total_blue_sheets = n * 8

# Calculate the number of notebooks needed for each color
notebooks_red = (total_red_sheets + k - 1) // k
notebooks_green = (total_green_sheets + k - 1) // k
notebooks_blue = (total_blue_sheets + k - 1) // k

# Total notebooks needed
total_notebooks = notebooks_red + notebooks_green + notebooks_blue

# Output the result
print("Minimum number of notebooks needed:", total_notebooks)