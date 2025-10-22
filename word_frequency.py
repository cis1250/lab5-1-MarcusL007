#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def isValid():
    user_sentence = input("Enter a sentence: ")
    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    user_sentence = re.sub(r'[^A-Za-z ]', '', user_sentence)
    return user_sentence

def calculate_frequencies(user_sentence):
    sentence = user_sentence.split(" ")

    words = []
    count = []

    for word in sentence:
        if word not in words:
            words.append(word.lower())
            count.append(0)
    for word in sentence:
        index = words.index(word.lower())
        count[index] += 1

    return words, count

def print_frequencies(words, frequencies):
    for i in range(len(words)):
        print(words[i] + ": " + str(frequencies[i]))

def main():
    user_sentence = isValid()
    
    words, count = calculate_frequencies(user_sentence)

    print_frequencies(words, count)
    

main()
