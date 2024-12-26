#Write a Python function that accepts arbitrary parameters and calculates the sum of factorial of all the integers passed as arguments. The function should handle a variable number of arguments and return the sum.
def f(*args):
    for i in args:
        fact=1
        sum=0
        for j in range(1,i+1):
            fact*=j
            sum=sum+fact
    print(sum)
f(1,2,3,4)