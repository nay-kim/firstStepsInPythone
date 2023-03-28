# This program askes for my name
# playing with while function
# be careful here we have function with nfinite loop
name = ""
while True:
    print ("Pleas enter 'your name'.")
    name = input ()
    if name == "your name":
        break
print ("Thank you!", name)