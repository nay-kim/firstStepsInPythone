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
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....  (its look like revers grid)
# Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0].
# This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
# The last thing your program will print is grid[8][5].
#
# Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.

import copy

# function declaration.

def diagonalFlipp_wl(grid):
    # Code that diagonally flips the grid list by vertically adding horizontal values in a new list.
    flippedGrid = []
    harts = []
    for x in range(len(grid[0])):
        flippedList = []
        for y in range(len(grid)):
            flipped = copy.copy(grid[y][x])
            flippedList.append(flipped)
        flippedGrid.append(flippedList)
    harts = [flippedGrid, grid]
    return harts

def printHart(harts):
    # Code that list elements on separate lines.
    for number, hart in enumerate(harts):
        print("")
        print("The hart figure number ", number+1)
        print("")
        for index, item in enumerate(hart):
            print(item)

# The program.

printHart(diagonalFlipp_wl(
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]))
