sudoku_puzzle = [[3, 9, '_', '_', 5, '_', '_', '_', '_'],
                 ['_', '_', '_', 2, '_', '_', '_', '_', 5],
                 ['_', '_', '_', 7, 1, 9, '_', 8, '_'],
                 ['_', 5, '_', '_', 6, 8, '_', '_', '_'],
                 [2, '_', 6, '_', '_', 3, '_', '_', '_'],
                 ['_', '_', '_', '_', '_', '_', '_', '_', 4],
                 [5, '_', '_', '_', '_', '_', '_', '_', '_'],
                 [6, 7, '_', 1, '_', 5, '_', 4, '_'],
                 [1, '_', 9, '_', '_', '_', 2, '_', '_']]
        
        
# find an empty cell in the sudoku puzzle
# check the row, column and the 3x3 box of that cell to know if it's correct
# once correct move forward, else try another number
# if no options anymore, backtrack and try another number on the previous cell
# until come up with a solution
# repeat until all cells are filled 

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
        return True

    row, column = empty_cell
    for i in range(1, 10):
        if try_check(board, empty_cell, i):
            board[row][column] = i
            
            if final_solve(board):
                return True
            else:
                board[row][column] = '_'
    return False
        
display_board(sudoku_puzzle)
final_solve(sudoku_puzzle)
print('-----------------------------------')
display_board(sudoku_puzzle)
