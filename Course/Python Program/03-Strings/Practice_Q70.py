#Write a Python program to count the occurrences of each word in a given sentence.
def count_word_occurrences(sentence):
    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()
    
    # Create a dictionary to store the word counts
    word_count = {}
    
    # Loop through each word in the list and update the count
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Example usage
sentence = "Hello world! This is a test. Hello again!"
result = count_word_occurrences(sentence)

print(f"Word occurrences: {result}")
