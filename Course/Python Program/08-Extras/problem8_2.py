# Vitya has just started learning Berlanese language. It is known that Berlanese uses the Latin alphabet. Vowel letters are "a", "o", "u", "i", and "e". Other letters are consonant.

# In Berlanese, there has to be a vowel after every consonant, but there can be any letter after any vowel. The only exception is a consonant "n"; after this letter, there can be any letter (not only a vowel) or there can be no letter at all. For example, the words "harakiri", "yupie", "man", and "nbo" are Berlanese while the words "horse", "king", "my", and "nz" are not.

# Help Vitya find out if a word s is Berlanese

def is_berlanese(word):
    vowels = "aeiou"
    n = len(word)

    for i in range(n):
        if word[i] not in vowels:  # If the character is a consonant
            if word[i] != 'n':  # If it's not 'n'
                # Check if it's the last character or the next character is not a vowel
                if i == n - 1 or word[i + 1] not in vowels:
                    return False
    return True

def main():
    # Input from the user
    word = input("Enter a word: ").strip()
    
    if is_berlanese(word):
        print(f"{word} is a Berlanese word.")
    else:
        print(f"{word} is not a Berlanese word.")

if __name__ == "__main__":
    main()
