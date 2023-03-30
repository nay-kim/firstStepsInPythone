# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list (n=100) of heads and tails.
# Your program breaks up the experiment into two parts:
# 1) the first part generates a list of randomly selected 'heads' and 'tails' values,
# 2) and the second part checks if there is a streak in it.
# Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row.
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

# just as program

import random

# variable declaration

numberOfStreaks = 0
numberOfExperiment = 10000
listOfExperiments = []

for experimentNumber in range(numberOfExperiment):

    # Code that creates a list of 100 'heads' or 'tails' values.
    experiment = []  # Create a new list of 100 'heads' or 'tails' values.
    for itemNumber in range(100):
        if random.randint(0, 1) == 0:
            experiment.append("H")  # Add a 'heads' value.
        else:
            experiment.append("T")  # Add a 'tails' value.

        # Code that checks if there is a streak of 6 heads or tails in a row.
        if itemNumber == 0:  # is first item.
            result = 0  # Create a value to calculate a number of sequential equal items.
        else:
            if experiment[itemNumber] == experiment[itemNumber - 1]:
                result = result + 1  # Increas result value to 6.
                if result == 5:
                    numberOfStreaks = numberOfStreaks + 1
                    streak = 0  # Calculation reset.
            else:
                result = 0

    listOfExperiments.append(experiment)  # listOfExperiments is a list of experiment lists.

portionOfStreaks = (numberOfStreaks / numberOfExperiment) * 100

print("The portion of Streaks in ", numberOfExperiment, " experiments is:", portionOfStreaks, "%")