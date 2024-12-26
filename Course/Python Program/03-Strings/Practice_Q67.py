#Write a Python Program to Detect if Two Strings are Anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
str1 = "Listen"
str2 = "Silent"

if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")
