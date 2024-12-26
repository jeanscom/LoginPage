# You are designing a Python function for calculating the volume of a box. The box has 
# different dimensions: length, width, and height. You want to provide flexibility in the 
# order of arguments when calling the function using keyword arguments. Write a 
# Python function calculate_volume that accepts these dimensions as keyword 
# arguments and calculates the volume of the box
a=int(input("Enter the lenght: " ))
b=int(input("Enter the width: "))
c=int(input("Enter the height: "))
def v(*z):
    s=a*b*c
    print('volume of the cube is',s)
v(a,b,c)