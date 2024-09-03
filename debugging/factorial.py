#!/usr/bin/python3

import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
        return result

#Check if an argument is provided
if len(sys.argv) < 2:
    print("Error: Please provide a number as a command-line argument.")
    sys.exit(1) #Exit the program with an error code

try:
    #try to convert the first command-line argument to an integer
    number = int(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1) #Exit the program with an error code

#calculate the fatorial and print the result
f = factorial(number)
print(f)
