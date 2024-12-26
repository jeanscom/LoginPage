
# Write a Python program to compute the sum of the following series:
# S = 1 + (x^2)/2! + (x^4)/4! + (x^6)/6! + ... + (x^2n)/n!
# The program should have the following subfunctions:
# calculate_factorial(n): This function calculates the factorial of a given positive integer
# n.
# calculate_term(x, n): This function computes the individual term of the series for a
# given x and n.
# calculate_series_sum(x, n): This function calculates and returns the sum of the series
# up to the nth term.
# In the main part of the program, take the values of x and n as input from the user
# and use the subfunctions to compute the sum of the series. Finally, display the
# result.
def calculate_factorial(n):
    z=1
    for i in range(1,n+1):
        z*=i
    return z
def calculate_team(x,n):
    z=calculate_factorial(n)
    a=(x**(2*n))/z
    return a
def calculate_series_sum(x,n):
    s=0
    for i in range(0,n+1,):
        q=calculate_team(x,i)
        s+=q
    print(s)
calculate_series_sum(1,4)
