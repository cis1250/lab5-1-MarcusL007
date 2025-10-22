#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def validCheck(amount):
    if amount.isalpha() == True or int(amount) <= 0:
        print("Please enter a positive integer.")
        return True
    else:
        return False
        
def generate(amount):
    fib = "0 1 "
    first = 0
    second = 1
    for i in range(int(amount) - 2):
        fib += str(first + second) + " "
        temp = first + second
        first = second
        second = temp
    return fib

def fibonacci():
    while True:
        amount = input()
        if not validCheck(amount):
            print(generate(amount))
            break

fibonacci()
