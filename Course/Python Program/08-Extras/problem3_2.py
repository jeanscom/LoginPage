# Implement a Library Management System using tuples in Python. This system allows
# you to add books, display the available books, and search for a book:n this example,
# each book is represented as a tuple with the elements (title, author, genre). The
# add_book function appends a new book to the library, display_books prints all
# available books, and search_book searches for a book by title.
# Strings
# Take a 200 word paragraph text as input. (You may initialize it within the program). Perform the below 
# operations on the string.
# • Convert the words into upper and lower case
# • Word Count: count the number of words in the text
# • Character Count: Count the total number of characters in the text.
# • Most Common Word: Find and print the most common word in the text.
# • Palindrome Check: check if the given text is a palindrome.
# • Replace Substring: Take a substring as input and a replacement string, then
# replace all occurrences of the substring in the text with the replacement
# string.
# • Sentence Capitalization: Capitalizes the first letter of each sentence in the
# text.
# • Vowel Count: Count the number of vowels and consonants in the text.
# • Consonant Count: Count the number of consonants in the text.
# • Display Unique Words: Display all unique wordsin the text.
# • Reverse Words in a String: Reverse the order of words in a given string.
# • Check whether two strings are anagrams or not : anagram is a word or
# phrase formed by rearranging the letters of another word or phrase, using all
# the original letters exactly once. In other words, two strings are considered
# anagrams if they have the same characters with the same frequency, but the
# order of the characters can be different.
# 1. For example:
# 2. "listen" and "silent" are anagrams.
# 3. "heart" and "earth" are anagrams.
# 4. "python" and "typhon" are anagrams.
# 5. To check if two strings are anagrams

# Library Management System
def add_book(library, title, author, genre):
    book = (title, author, genre)
    library.append(book)
    print(f"Book '{title}' added successfully!\n")

def display_books(library):
    if not library:
        print("No books available in the library.\n")
        return
    print("Available Books:")
    for book in library:
        print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
    print()

def search_book(library, title):
    for book in library:
        if book[0].lower() == title.lower():
            print(f"Book found: Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}\n")
            return
    print(f"Book '{title}' not found in the library.\n")

def main_library_system():
    library = []
    
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Display Available Books")
        print("3. Search for a Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            add_book(library, title, author, genre)
        elif choice == '2':
            display_books(library)
        elif choice == '3':
            title = input("Enter the title of the book to search: ")
            search_book(library, title)
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# String Operations
def string_operations():
    text = ("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. "
            "Lorem ipsum may be used as a placeholder before the final copy is available.")
    
    print("Original Text:\n", text)
    
    # Convert to upper and lower case
    print("\nUpper Case:\n", text.upper())
    print("\nLower Case:\n", text.lower())
    
    # Word Count
    word_count = len(text.split())
    print("\nWord Count:", word_count)
    
    # Character Count
    char_count = len(text)
    print("Character Count:", char_count)
    
    # Most Common Word
    from collections import Counter
    words = text.split()
    most_common_word = Counter(words).most_common(1)[0]
    print("Most Common Word:", most_common_word[0], "occurs", most_common_word[1], "times")
    
    # Palindrome Check
    is_palindrome = text == text[::-1]
    print("Is the text a palindrome?", is_palindrome)
    
    # Replace Substring
    substring = input("\nEnter a substring to replace: ")
    replacement = input("Enter the replacement string: ")
    new_text = text.replace(substring, replacement)
    print("Text after replacement:\n", new_text)
    
    # Sentence Capitalization
    capitalized_text = '. '.join(sentence.capitalize() for sentence in text.split('. '))
    print("\nCapitalized Sentences:\n", capitalized_text)
    
    # Vowel and Consonant Count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    print("Vowel Count:", vowel_count)
    print("Consonant Count:", consonant_count)
    
    # Display Unique Words
    unique_words = set(words)
    print("Unique Words:", unique_words)
    
    # Reverse Words in a String
    reversed_words = ' '.join(reversed(words))
    print("Reversed Words:\n", reversed_words)
    
    # Anagram Check
    str1 = input("\nEnter first string to check for anagram: ")
    str2 = input("Enter second string to check for anagram: ")
    is_anagram = sorted(str1) == sorted(str2)
    print(f"Are '{str1}' and '{str2}' anagrams?", is_anagram)

if __name__ == "__main__":
    print("Welcome to the Library Management System!")
    main_library_system()
    print("\nNow performing string operations...")