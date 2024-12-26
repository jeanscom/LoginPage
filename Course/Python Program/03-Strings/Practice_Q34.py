#Write a Python program to print all ASCII characters with their values.
# Print all ASCII characters with their values
for i in range(32, 127):  # ASCII printable characters are from 32 to 126
    print(f"ASCII value of '{chr(i)}' is {i}")

