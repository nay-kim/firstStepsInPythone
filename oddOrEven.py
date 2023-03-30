# Automate the Boring Stuff with Python chapter 3 final problem
# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

import random

def collatz():
    if number % 2 == 0:
        print("number // 2 = ", number // 2)
    else:
        print("3 * number + 1 = ",  3 * number + 1)

number = random.randint(0, 100)
print(number)
collatz()