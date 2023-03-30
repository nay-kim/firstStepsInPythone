# this program askes me how many cates do I have
# this code is an example of exception handling
# alwaus refer to user cases
print("How many cats do you have")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That is a lot.")
    else:
        print("You are good.")
except ValueError:
    print("pleas enter a number")