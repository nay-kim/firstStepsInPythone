print("Hello world")
print("I am learning pythone")
print ("Those are my notes for - Automate the Boring Stuff with Python book")
print("")

print("Standard comperison operations")
a = 3 == 2 + 1
print("a = 3 == 2 + 1, a =", a)
b = 3 != 2 + 1
print("b = 3 != 2 + 1, b =", b)
c = 3 > 2 + 1
print("c = 3 > 2 + 1, c =", c)
d = 3 < 2 + 1
print("d = 3 > 2 + 1, d =", d)
e = 3 <= 2 + 1
print("e = 3 <= 2 + 1, e =", e)
f = 3 >= 2 + 1
print("f = 3 >= 2 + 1, f =", f)
g = 3 == "3"
print("g = 3 == str(3), g =", g)
h = 3 == 3.0
print("g = 3 == 3.0, g =", h)
print("")

print("Truth table")
x = True
y = False
i = x and x
j = x and y
k = y and x
l = y and y
print(x, "and", x, "=", i)
print(x, "and", y, "=", j)
print(y, "and", x, "=", k)
print(y, "and", y, "=", l)
m = x or x
n = x or y
o = y or x
p = y or y
print(x, "or", x, "=", m)
print(x, "or", y, "=", n)
print(y, "or", x, "=", o)
print(y, "or", y, "=", p)
print("")

print("value comperison")
myAge = 26
myPet = "cat"
compAgePet = myAge > 20 and myPet == "cat"
print (compAgePet)