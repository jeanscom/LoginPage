#. Write a user defined function to print the message Namasthe n times, where n is a parameter.
def f():
    s="Namaste"
    n=int(input())
    print("Namaste")
    s=s+n*"Namaste"
    return s
f()