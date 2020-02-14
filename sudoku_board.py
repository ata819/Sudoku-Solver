

board_format = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# This solve function uses recursive back tracking
def solve(board):
    # Searches for an empty slot, and returns that position
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if board_validation(board, i, (row, column)):
            board[row][column] = i
            # Checks if solution is valid, returns true
            if solve(board):
                return True
            # Else resets the previous solution and starts over
            board[row][column] = 0

    return False

# Used to validate the board provided. If the board is "unsolvable", it will return false
# By unsolvable, it means the board provided does not follow the rules of sudoku. 1-9 rows, columns, quadrants.
def board_validation(board, num, sect):
    # Checks the rows, Makes sure that for 1 row, all the numbers are different
    for i in range(len(board[0])):
        if board[sect[0]][i] == num and sect[1] != i:
            return False
    # Checks the column, Makes sure that all the numbers for that column are different
    for i in range(len(board)):
        if board[i][sect[1]] == num and sect[0] != i:
            return False

    x_box = sect[1] // 3
    y_box = sect[0] // 3
    # Checks the cube quadrants(9) to make sure the numbers are all different
    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box*3, x_box*3 + 3):
            if board[i][j] == num and (i, j) != sect:
                return False
    return True


# i represents the vertical (row count) and the j represents the horizontal (column count)
def board_print(board):
    # Separates top, middle, and bottom quadrants
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        # Separates left, middle, and right quadrants
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # prints 8 numbers, else print last number and nl
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Searches for an empty slot 1 - 81
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


board_print(board_format)
solve(board_format)
print("#########SOLVED##########")
board_print(board_format)