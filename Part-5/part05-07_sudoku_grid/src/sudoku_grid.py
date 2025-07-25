def row_correct(sudoku: list, row_no: int):
    for number in sudoku[row_no]:
        if number == 0:
            continue
        if sudoku[row_no].count(number) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        if row[column_no] == 0:
            continue
        column.append(row[column_no])
    
    for number in column:
        if column.count(number) >1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    grid = []
    for row in sudoku[row_no: row_no + 3]:
        for number in row[column_no: column_no + 3]:
            if number == 0:
                continue
            grid.append(number)
    for n in grid:
        if grid.count(n) > 1:
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)):
        if row_correct(sudoku, i) == False:
            return False
    for j in range(len(sudoku)):
        if column_correct(sudoku, j) == False:
            return False

    for l in [0,3,6]:
        for k in [0,3,6]:
            if block_correct(sudoku, l, k) == False:
                return False
    return True
        

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))