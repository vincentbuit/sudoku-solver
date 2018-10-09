# Check if the sudoku is solved. Boolean
def is_solved(sudoku):
    for y in range(0, 9):
        if 0 in sudoku[y]:
            return False
    return True
