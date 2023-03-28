# playing with while function
# breaking and continuing the loops
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print ("spam is" +" "+ str(spam))
print ("")

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        break
    print ("spam is" +" "+ str(spam))