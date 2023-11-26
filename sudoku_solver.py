'''''
                                                    'SUDOKU SOLVER'
solving the sudoku using backtracking:
-initially we check the empty spots in the sudoku board
-checking the numbers 1 to 9 in the empty places
  '''''


# Sudoku Solver using Backtracking Algorithm

# The input Sudoku board is represented as a 9x9 matrix.
# Empty cells are indicated with 0.

# Define the input Sudoku board
board = [
    [4, 7, 0, 1, 0, 0, 0, 0, 3],
    [6, 0, 0, 5, 0, 3, 0, 0, 0],
    [0, 0, 5, 0, 7, 9, 0, 2, 0],
    [0, 1, 0, 7, 0, 6, 2, 0, 0],
    [0, 5, 0, 0, 0, 8, 9, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [7, 0, 3, 0, 0, 5, 0, 0, 1],
    [2, 4, 8, 0, 9, 0, 6, 0, 0]
]

# Function to print the Sudoku board
def print_board(bo):
    # Add horizontal lines to separate 3x3 subgrids
    for i in range(len(bo)):
        if i % 3 == 0:
            print("- " * 12)
        for j in range(len(bo[0])):
            # Add vertical lines to separate 3x3 subgrids
            if j % 3 == 0:
                print("| ", end="")
            # Print the cell value
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# Function to find the first empty cell (cell with value 0)
def find_empty_cell(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

# Function to check if a number is valid to place in a specific position
def is_valid(bo, num, pos):
    # Check if the number is not in the same row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check if the number is not in the same column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check if the number is not in the same 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

# Main function to solve the Sudoku puzzle using backtracking
def solve_sudoku(bo):
    empty_cell = find_empty_cell(bo)
    # If no empty cells are found, the Sudoku is solved
    if not empty_cell:
        return True
    else:
        row, col = empty_cell
    for num in range(1, 10):
        if is_valid(bo, num, (row, col)):
            bo[row][col] = num
            if solve_sudoku(bo):
                return True
            bo[row][col] = 0
    return False

# Call the solve_sudoku function to solve the Sudoku board
solve_sudoku(board)

# Print the solved Sudoku board
print_board(board)
