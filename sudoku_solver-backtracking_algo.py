sudoku_puzzle = []

def display_board(board):
    print('+' * 31)
    for i in range(len(board)):
        print('|', end='')
        for j in range(len(board[i])):
            print(' ' + str(board[i][j]) + ' ', end='')
            if (j + 1) % 3 == 0:
                print('|', end='')
        print()
        if (i+1) % 3 == 0:
            print('+' * 31)
            
def find_empty_blocks(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return (i,j)
    return None
            
def try_check(board, location, number):
    row, column = location
    # checking the row
    if number in board[row]:
        return False
    
    # check column
    for i in range(len(board[row])):
        if board[i][column] == number:
            return False
    
    # check the 3x3 box 
    row = row // 3 * 3 
    column = column // 3 * 3
    
    for i in range(row, row+3):
        for j in range(column, column+3):
            if board[i][j] == number:
                return False
    return True

def final_solve(board):
    empty_cell = find_empty_blocks(board)
    if empty_cell == None:
        return display_board(board)

    row, column = empty_cell
    for i in range(1, 10):
        if try_check(board, empty_cell, i):
            board[row][column] = i
            
            if final_solve(board):
                return True
            else:
                board[row][column] = '_'
    return False
    

def input_puzzle():
    print("\nInput the puzzle by rows.\n")
    for i in range(9):
        sudoku_puzzle.append(list(input().rstrip().split()))
        for j in range(len(sudoku_puzzle[i])):
            if ord(sudoku_puzzle[i][j]) >= 49 and ord(sudoku_puzzle[i][j]) <= 57:
                sudoku_puzzle[i][j] = int(sudoku_puzzle[i][j])
    

def intro():
    print("""███████ ██    ██ ██████   ██████  ██   ██ ██    ██     ███████  ██████  ██      ██    ██ ███████ ██████  
██      ██    ██ ██   ██ ██    ██ ██  ██  ██    ██     ██      ██    ██ ██      ██    ██ ██      ██   ██ 
███████ ██    ██ ██   ██ ██    ██ █████   ██    ██     ███████ ██    ██ ██      ██    ██ █████   ██████  
     ██ ██    ██ ██   ██ ██    ██ ██  ██  ██    ██          ██ ██    ██ ██       ██  ██  ██      ██   ██ 
███████  ██████  ██████   ██████  ██   ██  ██████      ███████  ██████  ███████   ████   ███████ ██   ██ 

1. Stuck in a sudoku puzzle? Wanted to know what block/s you got wrong?
2. Input the sudoku puzzle (type/use '_' if that block is empty)""")
    input_puzzle()
    display_board(sudoku_puzzle)
    print('=' * 31)
    print('Solved!')
    final_solve(sudoku_puzzle)
    

intro()
