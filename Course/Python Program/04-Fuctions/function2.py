#Write a function to return the reverse of the number entered.
#Example: Reverse of number 1234 displays 4321
def f(num):
    rev_num=""
    for i in (str(num)):
        rev_num=i+rev_num
    print(rev_num)
f(1234)