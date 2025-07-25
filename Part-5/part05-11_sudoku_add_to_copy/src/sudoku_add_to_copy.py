def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i in [0,3,6]:
            print()
        for j in range(len(sudoku[i])):
            if j in [3,6]:
                if sudoku[i][j] > 0:
                    print(f" {sudoku[i][j]} ", end="")
                else:
                    print(" _ ", end="")
            else:    
                if sudoku[i][j] > 0:
                    print(f"{sudoku[i][j]} ", end="")
                else:
                    print("_ ", end="")
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    s = [row[:] for row in sudoku]

    s[row_no][column_no] = number
    return s

if __name__ =="__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)