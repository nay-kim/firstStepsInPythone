# this code is an example of function definition
def hello():
    print("de-dublication!")
    print("Howdy!")
    print("blaa blaaaa!")
    print("blaa blaaaa Howdy!")

hello()
print("")
hello()
print("")

# this code is an example of function definition with string parameter
def name(name):
    print("hello" + " " + name)

name("Alice")
name("Bob")
print("")

# this code is an example of function definition with numeric parameter
def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)