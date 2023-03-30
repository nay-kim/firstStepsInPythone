# For practice, write programs to do the following tasks.
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.
# Be sure to test the case where an empty list [] is passed to your function.

#initial version tjat is not thet good - see string-list.py

def generateList():
    while True:
        print("Enter the " + str(len(spam) + 1) + " item of list. Or enter nothing to stop")
        name = input()
        if name == '':
            break
        spam.append(name)

def listValueArgument():
    try:
        print("You created the list with " + str(len(spam)) + " items.")
        for i in range(0, len(spam) - 1):
            print(spam[i], ", ", end="")
        print("and ", spam[len(spam) - 1])
    except IndexError:
        print("The generated list is empty or has insufficient number of items. Please enter List items one by one.")

spam = []
generateList()
listValueArgument()