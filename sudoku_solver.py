'''''
                                                    'SUDOKU SOLVER'
solving the sudoku using backtracking:
-initially we check the empty spots in the sudoku board
-checking the numbers 1 to 9 in the empty places
-if the number we inserted dis wrong then we backtrack and try another number
-backtracking goes on till the last place to be filled and solves the board    '''''
board=[]
# Enter the input in a 9*9 matrix format and represent the numbers which has to be find with 0

for i in range(9):
    board.append([int(j) for j in input().split()])

# print_board function helps to print the  solved sudoku
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            print("- " * 12)
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print("| ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# finding all the 0's i.e., the numbers which has to be filled
def empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

#checking the number which we entered is valid  or not
def valid(bo, num, pos):
    # validating the number is not present in the row of the sudoku board
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        # validating the number is not present in the column of the sudoku board
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # validating the number is not present in the box i.e., 3*3 where the range of 1 to 9 are present
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

#solving the sudoku using backtracking
def solve(bo):
    #reetriving the position of the empty places i.e., 0's
    find = empty(bo)
    #if no empty positions left then the board is solved and returns true
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        #validating
        if valid(bo, i, (row, col)):
            #checking each number from 1 to 9
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False

#calling the solve function and solves the board
solve(board)
#printing the solved sudoku board
print_board(board)
