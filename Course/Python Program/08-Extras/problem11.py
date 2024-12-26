# Bailey is known to be a very intelligent German Shepherd puppy. Bailey is 
# very particular about the food that he eats. He only likes Carrot, Royal Canin 
# and Toblerone. However, Bailey is stubborn today. He will only eat two 
# consecutive Toblerone at a time. If he is given one Toblerone chocolate, he will 
# refuse to eat. Although he is stubborn, he is very sweet and playful after having 
# his food. Can you help Bailey in checking whether he can eat or not? Carrot is 
# represented as 1, Royal Canin is represented as 2 and Toblerone is represented 
# as 3. 
# Input 
# 1 2 2 2 3 1 3 3 2 1 3 
# Output 
# Yes

# Input food items as a string
input_food = "1 2 2 2 3 1 3 3 2 1 3"

# Convert the input string to a list of integers
food_list = list(map(int, input_food.split()))

# Initialize a variable to track if Bailey can eat
can_eat = False

# Check for consecutive Toblerone (3)
for i in range(len(food_list) - 1):
    if food_list[i] == 3 and food_list[i + 1] == 3:
        can_eat = True
        break  # No need to check further if we found a pair

# Output the result
if can_eat:
    print("Yes")
else:
    print("No")