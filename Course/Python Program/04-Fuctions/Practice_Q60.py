#Write a Python program that invokes a given function after specific milliseconds.
import time

def my_function():
    print("Function has been invoked!")

def invoke_after(milliseconds):
    # Convert milliseconds to seconds
    seconds = milliseconds / 1000
    # Wait for the specified time before invoking the function
    time.sleep(seconds)
    # Invoke the function
    my_function()

# Example usage: Invoke `my_function` after 2000 milliseconds (2 seconds)
invoke_after(2000)
