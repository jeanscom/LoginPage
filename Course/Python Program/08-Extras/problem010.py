# Alice and Bob are decorating a Christmas Tree.

# Alice wants only 3 types of ornaments to be used on the Christmas Tree: yellow, blue and red. They have y yellow ornaments, b blue ornaments and r red ornaments.

# In Bob's opinion, a Christmas Tree will be beautiful if:

# the number of blue ornaments used is greater by exactly 1 than the number of yellow ornaments, and the number of red ornaments used is greater by exactly 1 than the number of blue ornaments. That is, if they have 8 yellow ornaments, 13 blue ornaments and 9 red ornaments, we can choose 4 yellow, 5 blue and 6 red ornaments (5=4+1 and 6=5+1 ).

# Alice wants to choose as many ornaments as possible, but she also wants the Christmas Tree to be beautiful according to Bob's opinion.

# In the example two paragraphs above, we would choose 7 yellow, 8 blue and 9 red ornaments. If we do it, we will use 7+8+9=24 ornaments. That is the maximum number.

# Since Alice and Bob are busy with preparing food to the New Year's Eve, they are asking you to find out the maximum number of ornaments that can be used in their beautiful Christmas Tree!

# It is guaranteed that it is possible to choose at least 6 (1+2+3=6 ) ornaments.
# Input: number of yellow, blue, and red ornaments

Y = int(input("Enter the number of yellow ornaments: "))
B = int(input("Enter the number of blue ornaments: "))
R = int(input("Enter the number of red ornaments: "))

# Calculate the maximum number of yellow ornaments that can be used
max_yellow = min(Y, B - 1, R - 2)

# Calculate the total number of ornaments used
total_ornaments = 3 * max_yellow + 3

# Output the result
print("Maximum number of ornaments that can be used:", total_ornaments)