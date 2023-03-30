# function oriented

# Say you have a list of lists where each value in the inner lists is a one-character string, like this:
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters.
# The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

# Copy the previous grid value, and write code that uses it to print the image.
# ....OOOO..OOOO....
# ..OOOOOOOOOOOOOO..
# ..OOOOOOOOOOOOOO..
# ....OOOOOOOOOO....
# ......OOOOOO......
# ........OO........  (its look like revers grid*2)
# Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0].
# This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
# The last thing your program will print is grid[8][5].
#
# Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.
#
# Additional tasks: enlarged heart 2 times after flipping and replace "0" with "." and vice versa.

import copy

# function declaration.

def diagonalFlipp_wl(grid):
    # Code that diagonally flips the grid list by vertically adding horizontal values in a new list.
    flippedGrid = []  # this list is a final flipped list to care a heart shape.
    for x in range(len(grid[0])):  
        flippedList = []  
        for y in range(len(grid)):  
            flipped = grid[y][x]  # we take items one by one moving upside down and assign them to other variable right to left. It creates a flip.
            flippedList.append(flipped)
            # For the multiplication, we can read this action but let's create a new function.
            # However, we can create more modular and maintainable code by breaking down complex tasks into smaller, more manageable functions.
        flippedGrid.append(flippedList)
    harts = [grid, flippedGrid]  # to return multiple valuse refer to a list format.
    return harts

def multiply(harts, n = 2):
    # Code that multiplies the items in a list by n.
    flippedGrid = harts[1]
    typesOfHarts = []
    for y in range(len(flippedGrid)):  # Takes a list's items (internal lists) one by one. Direction doesnt metter here. 
        duplicatFlippedLine = []
        for x in range(len(flippedGrid[0])):  # Takes internal list items one by one.
            duplicat = flippedGrid[y][x]
            for enlage in range(0, n):  # As need to multiply horisontally, add the selected item in another list n times.
                duplicatFlippedLine.append(duplicat)  # Add internal lists items in internal lists.
        for elongate in range(0, n):  # As need to multiply vertically, add the selected line in another list n times.
            typesOfHarts.append(duplicatFlippedLine)  # Add internal lists in a final list that cares enlarged heart.
    hartsList = [harts[0], harts[1], typesOfHarts]  # To return multiple values refer to a list format. Organize lists by modification order.
    return hartsList

def itemExchange(hartsList):
    # Code that exchange item one by anoter - "." to "0" and vice versa.
    # I don't like this code too loopy.
    negativeHart = []
    for listNumber, list in enumerate(hartsList):
        negativeHartline = []
        for lineIndex, line, in enumerate(list):
            hartNegativeItem = []
            for index, item in enumerate(line):
                if item == ".":
                    hartNegativeItem.append("0")
                else:
                    hartNegativeItem.append(".")
            negativeHartline.append(hartNegativeItem)
        negativeHart.append(negativeHartline)
    return negativeHart

def printHart(hartsList):
    # Code that list elements on separate lines.
    for number, hart in enumerate(hartsList):  # take harts stored in list one by one.
        print("") 
        print("The hart figure number ", number+1)
        print("")
        for index, item in enumerate(hart):  # take each line that formed hart and print one by one.
            print(item)

# The program.

printHart(multiply(diagonalFlipp_wl(
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']])))

print("")
print("All harts in  negative mode")

printHart(itemExchange(multiply(diagonalFlipp_wl(
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]))))