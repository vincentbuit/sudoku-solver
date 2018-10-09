def find_y(sudoku):
    all_y_rows = []
    for x in range(0, 9):
        row = []
        for y in range(0, 9):
            row.append(sudoku[y][x])
        all_y_rows.append(row)
    return all_y_rows
