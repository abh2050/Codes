import hashlib
import time

import random
import string

# Number of words in the dictionary
n = 1000

# Length of each word
word_length = 12

# Create a list of random words
words = [''.join(random.choices(string.ascii_letters, k=word_length)) for _ in range(n)]

# Write the list of words to a file
with open("dictionary.txt", "w") as file:
    for word in words:
        file.write(word + "\n")


def crack_password(password_hash, dictionary):
    """
    Function to crack a password using a brute force method and a dictionary of possible passwords
    """
    start = time.time()
    with open(dictionary, "r") as file:
        for line in file:
            line = line.strip() # remove newline character
            hashed_word = hashlib.md5(line.encode()).hexdigest()
            if hashed_word == password_hash:
                end = time.time()
                print(f"Password found: {line}")
                print(f"Time taken: {end - start} seconds")
                return
    end = time.time()
    print("Password not found in dictionary.")
    print(f"Time taken: {end - start} seconds")

# Example usage
crack_password("5f4dcc3b5aa765d6327deb882cf99", "dictionary.txt")
