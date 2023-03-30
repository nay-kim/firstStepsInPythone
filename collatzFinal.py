# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.0

# Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.

def collatz(number):
    if int(number) % 2 == 0:
        print("Your number_1 is even")
        print("number_1 // 2 = ", int(number) // 2)
        return int(number) // 2
    else:
        print("Your number is odd")
        print("3 * number_1 + 1 = ",  3 * int(number) + 1)
        return 3 * int(number) + 1

print("enter any posutive number")
number = input()

try:
    while collatz(number) != 1:
        print(" ")
        print("enter any posutive number")
        number = input()

except ValueError:
    print ("You entered value with wrong format. Please enter a positive integer.")

print("Thank you!")