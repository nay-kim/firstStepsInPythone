# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list (n=100) of heads and tails.
# Your program breaks up the experiment into two parts:
# 1) the first part generates a list of randomly selected 'heads' and 'tails' values,
# 2) and the second part checks if there is a streak in it.
# Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row.
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

# function based aproch 

import random

# function declaration

def to_string(experiment):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for itemNumber in range(100):
        if random.randint(0, 1) == 0:
            experiment.append("H")  # Add a 'heads' value.
        else:
            experiment.append("T")  # Add a 'tails' value.
    return experiment

def to_check(experiment, numberOfStreaks=0, streak = 0):
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for itemNumber in range(len(experiment)):
        if experiment[itemNumber] == experiment[itemNumber - 1]:  # checks if current list item is the same as before
            streak += 1  # Increase result value to 6.
            if streak == 5:
                numberOfStreaks += 1  # Calculate number of streak of six heads or a streak of six tails.
                streak = 0 # Calculation reset.
        else:
            streak = 0  # Calculation reset.
    return numberOfStreaks

def to_streaksCount(streaksCount=0):
    # Code that increase the number Of Streaks by number Of Streaks every iteration.
    for numberOfExperiments in range(10000):
        result = (to_check(to_string([])))
        streaksCount += result
    return streaksCount

def to_portion(streaksCount, numberOfExperiments=10000):
    streakTotalP = (100/6)*numberOfExperiments
    portion = (streaksCount/streakTotalP)*100
    print("The portion of Streaks in 100 item list for ", numberOfExperiments, " experiments is: ", portion)

to_portion(to_streaksCount())