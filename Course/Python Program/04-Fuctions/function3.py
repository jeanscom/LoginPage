#A positive integer is entered through the keyboard. Write a function to obtain the factors of the given numbers.
def f(a):
    for i in range(1,a+1):
        if a%i==0:
            print(i,end=",")
f(8)