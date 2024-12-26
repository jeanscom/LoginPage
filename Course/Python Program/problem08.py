"""
(a) 	(b)	(C)
1	1	111
12	12	1221
123	123	123321
1234	1234	12344321
12345	12345	1234554321
(d)	(e)	(f)
12345	1	 1
1234	121	 121
123	12321	 12321
12	1234321	 121
1	1234543211	
"""
#a
    print("Pattern (a):")
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end="")
        print()  # Move to the next line
    print("\n")

#b
    print("Pattern (b):")
    for i in range(1, 6):
        for j in range(i):
            print(i, end="")
        print()  # Move to the next line
    print("\n")

#c
    print("Pattern (c):")
    for i in range(1, 6):
        # Print increasing part
        for j in range(1, i + 1):
            print(j, end="")
        # Print decreasing part
        for j in range(i, 0, -1):
            print(j, end="")
        print()  # Move to the next line
    print("\n")

#d
    print("Pattern (d):")
    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()  # Move to the next line
    print("\n")

#e
    print("Pattern (e):")
    for i in range(1, 6):
        # Print increasing part
        for j in range(1, i + 1):
            print(j, end="")
        # Print decreasing part
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()  # Move to the next line
    print("\n")

#f
    print("Pattern (f):")
    for i in range(1, 6):
        # Print increasing part
        for j in range(1, 6 - i + 1):
            print(j, end="")
        # Print decreasing part
        for j in range(5 - i + 1, 0, -1):
            print(j, end="")
        print()  # Move to the next line
    print("\n")

