# Solutione for Question 9 Chapter 2 Automate the Boring Stuff with Python
# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam
print ("enter any number srting from 0")
spam = input ()
if spam == "1":
    print ("Hellow")
elif spam == "2":
    print ("Howdy")
elif int(spam) >= int("3"):
    print ("Greetings")
print ("")