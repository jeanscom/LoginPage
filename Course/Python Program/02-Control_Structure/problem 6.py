
# One hot summer day Suraj Kumar and his friend Avinash Yadav decided to buy a
# watermelon. They chose the biggest and the ripest one weighing w kgs. They rushed
# hostel, dying of thirst, and decided to divide the melon, however they faced a hard
# problem. Both of them are great fans of even numbers, that’s why they want to
# divide the watermelon in such a way that each of the two parts weighs an even
# number of kilos, at the same time it is not obligatory that the parts are equal. The
# boys are extremely tired and want to start their meal as soon as possible, that’s why
# you should help them and find out if they can divide the watermelon in the way they
# want. For sure, each of them should get a part of the positiveweight. Print YES, if the
# boys can divide the watermelon into two parts or NO in the opposite case.

# Input number of test cases
T = int(input("Enter number of test cases: "))

# Process each test case
for _ in range(T):
    
   
    w = int(input("Enter the weight of the watermelon: "))

# Check if the weight is even and at least 4
    if w % 2 == 0 and w >= 4:
        print("YES")
    else:
        print("NO")	
