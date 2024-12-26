# Modify the above code to print the pattern as below. Take as input no: of rows

"""
a
1
22
333
4444
55555
666666
"""
for i in range(1, 7):
    for j in range(i):
        print(i, end='')  # Print the number without converting to string
    print()  # Move to the next line after each row


"""
b
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
