# A python program to solve 3x3 sudoku problems using recursion

# Import product from itertools, used here to compress multiple for loops
# into a single for loop when searching through the grid
from itertools import product

# Sample puzzle to solve, this is a maximum difficulty level puzzle from
# https://www.websudoku.com/?level=4
grid = [[3, 0, 0, 4, 9, 0, 0, 0, 0],
        [0, 5, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 6, 3, 0, 1, 0, 0],
        [8, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 3, 0, 0, 8, 0, 0, 7, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 4],
        [0, 0, 3, 0, 7, 8, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 3]]

# A function to check if there are any remaining empty squares
def checkGridFull(grid):
    # loop through each row and column, checking for empty squares
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    # if we dont find any empty squares, we have a full grid
    return True


# A function to check if the value has already been used in the current row
def usedInRow(value, row, grid):
    if value in grid[row]:
        return True
    else:
        return False


# A function to check if the value has already been used in the current column
def usedInColumn(value, col, grid):
    for r in grid:
        if r[col] == value:
            return True
    return False


# A function to check if the value has already been used in the current 3 x 3 subsquare
def usedInSubsquare(value, row, col, grid):
    rowMin = row // 3 * 3
    colMin = col // 3 * 3
    for r, c in product(range(0, 3), range(0, 3)):
        if grid[rowMin+r][colMin+c] == value:
            return True
    return False


# A function to check if the proposed move is valid
def validMove(value, row, col, grid):
    # check the value isn't used in the row first
    if not usedInRow(value, row, grid):
        # if not, check it isn't already used in the column
        if not usedInColumn(value, col, grid):
            # Finally, check it hasn't been used in the subsquare
            if not usedInSubsquare(value, row, col, grid):
                # If all tests are passed, return true (valid move) otherwise return false
                return True
    else:
        return False


# The recursive function used to solve the puzzle
def solvePuzzle(grid):
    # Find next empty cell
    for row, col in product(range(0, 9), range(0, 9)):
        if grid[row][col] == 0:
            # cycle through the possible moves, finding the first one that is valid
            for value in range(1, 10):
                if validMove(value, row, col, grid):
                    # tentatively assign the value to the square
                    grid[row][col] = value
                    # check if the puzzle has been finished
                    if checkGridFull(grid):
                        print("Grid completed!")
                        return True
                    # If not, recursively call this function, trying to finish the puzzle with the tentative value
                    else:
                        if solvePuzzle(grid):
                            return True
            # If a dead end is reached, and there are no valid moves, break this layer of recursion and backtrack to
            # the previous layer, where the next valid move will be attempted, if there are no remaining valid moves
            # in this layer the program will backtrack to the first layer where there is one.
            break
    # print out a backtrack notification message and remove the tentative value if backtracking through the layer
    print("Failed at row " + str(row) + ', col ' + str(col) + ", backtracking")
    grid[row][col] = 0

# Script to solve the puzzle
if solvePuzzle(grid):
    print('Sudoku puzzle successfully solved!')
    # Print the grid
    for r in grid:
        print(r)
    del r
else:
    print('Cannot solve sudoku puzzle')
