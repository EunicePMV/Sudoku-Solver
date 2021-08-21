# the following are techniques in solving a sudoku puzzle
def counting(sudoku=list):
    box = 0
    for i in range(len(sudoku_puzzle)):
        for j in range(3):
            # find the cell that don't have numbers
            if sudoku_puzzle[i][j] == '_':
                # getting the row and column where this belong
                cell_row = []
                cell_col = []
                for cell in range(len(sudoku_puzzle)):
                    cell_row += [sudoku_puzzle[i][cell]] # row of that cell
                    cell_col += [sudoku_puzzle[cell][j]] # column of that cell
                
                # finding the appropriate number for this cell by looking 
                # for the elements in missing_num
                row_col = cell_row + cell_col
                possible_num = list((set(missing_num[box*3//9]) - set(row_col)))
                
                # if in that cell there is only one possible number, then change that cell
                # into that possible number
                if len(possible_num) == 1:
                    sudoku_puzzle[i][j] = possible_num[0]
        box += 1

# get the input for the user's sudoku puzzle
sudoku_puzzle = []
for i in range(9):
    sudoku_puzzle.append(list(input().rstrip().split()))
    for j in range(len(sudoku_puzzle[i])):
        if ord(sudoku_puzzle[i][j]) >= 49 and ord(sudoku_puzzle[i][j]) <= 57:
            sudoku_puzzle[i][j] = int(sudoku_puzzle[i][j])
            
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
present_num = [[] for i in range(9)] 
by_col = [[] for i in range(9)]
missing_num = []
box = 0

# storing the present numbers in list
# arranging them in 3x3
for i in range(9):
    for j in range(3):
        if sudoku_puzzle[i][j]:
            present_num[box*3//9].append(sudoku_puzzle[i][j])
        if sudoku_puzzle[i][j+3]:
            present_num[box*3//9+3].append(sudoku_puzzle[i][j+3])
        if sudoku_puzzle[i][j+6]:
            present_num[box*3//9+6].append(sudoku_puzzle[i][j+6])
    box += 1
