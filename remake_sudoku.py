def remake_sudoku(sudoku):
    sudoku_current = []
    for a in range(0, 9):
        row_remake = []
        for b in range(0, 9):
            row_remake.append(sudoku[a][b])
        sudoku_current.append(row_remake)
    return sudoku_current
