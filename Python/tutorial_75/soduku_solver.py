LEN_BOARD = 9
board = [
    [0,3,0,5,0,0,4,0,0],
    [0,9,0,0,4,0,0,5,6],
    [4,0,0,0,0,0,0,2,0],
    [5,7,0,0,0,0,0,0,0],
    [0,6,4,0,3,1,2,0,0],
    [0,2,0,8,5,4,0,7,9],
    [8,0,7,6,0,0,9,0,3],
    [0,5,0,4,1,0,0,0,0],
    [0,1,0,3,8,9,0,0,0]
]


def solve(board : list):
    find = next_empty_space(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1,10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True
            else:
                board[row][col] = 0
    return False


def valid(board:list, num:int, pos:tuple):
    """
    Can the number be placed here?
    """
    row_pos, col_pos = pos
    # Check valid row
    for col in range(LEN_BOARD):
        if board[row_pos][col] == num and col_pos != col:
            return False

    # Check valid column
    for row in range(LEN_BOARD):
        if board[row][col_pos] == num and row_pos != row:
            return False

    # Check box
    start_box_x = (row_pos // 3) * 3
    start_box_y = (col_pos // 3) * 3
    print(start_box_x)
    print(start_box_y)
    for row in range(start_box_x, start_box_x + 3):
        for col in range(start_box_y, start_box_y + 3):
            if board[row][col] == num and (row,col) != pos:
                return False

    return True


def print_board(board : list):
    """
    Prints the board
    """
    for row in range(LEN_BOARD):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")

        for col in range(LEN_BOARD):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


def next_empty_space(board : list):
    """
    This finds a 0 on the board and returns the location
    If the board is full it returns None
    """
    for row in range(LEN_BOARD):
        for col in range(LEN_BOARD):
            if board[row][col] == 0:
                return (row, col)

    return None

print_board(board)
solve(board)
print("\n\n")
print_board(board)
if next_empty_space(board) != None:
    print("Invalid board")
