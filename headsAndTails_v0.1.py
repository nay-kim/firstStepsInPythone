# Internet suggestion

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list (n=100) of heads and tails.
# Your program breaks up the experiment into two parts:
# 1) the first part generates a list of randomly selected 'heads' and 'tails' values,
# 2) and the second part checks if there is a streak in it.
# Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row.
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

import random

#variable declaration

numberOfStreaks = 0
CoinFlip = []
streak = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        CoinFlip.append(random.randint(0,1))
    #does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(CoinFlip)):
        if CoinFlip[i] == CoinFlip[i-1]:  #checks if current list item is the same as before
            streak += 1
        else:
            streak = 0

        if streak == 6:  # But what if it is 12.
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))