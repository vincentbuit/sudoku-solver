from find_y import find_y
from find_sections import find_sections
import collections

def list_possibilities(one_list):
    possibilities = []
    dummy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 9):
        if dummy[i] not in one_list:
            possibilities.append(dummy[i])
    return possibilities


# Find the possible numbers (returns list) for a single unit
def find_possibilities(y, x, sudoku):
    # This field already has a number
    if sudoku[y][x] != 0:
        return False
    # Definitions
    y_row = find_y(sudoku)[x]
    x_row = sudoku[y]
    sections = find_sections(sudoku)
    # Find section
    if 0 <= y <= 2:
        if 0 <= x <= 2:
            section = sections[0]
        elif 3 <= x <= 5:
            section = sections[1]
        elif 6 <= x <= 8:
            section = sections[2]
    elif 3 <= y <= 5:
        if 0 <= x <= 2:
            section = sections[3]
        elif 3 <= x <= 5:
            section = sections[4]
        elif 6 <= x <= 8:
            section = sections[5]
    elif 6 <= y <= 8:
        if 0 <= x <= 2:
            section = sections[6]
        elif 3 <= x <= 5:
            section = sections[7]
        elif 6 <= x <= 8:
            section = sections[8]
    # Find possibilities which are possible in all 3 lists
    x_poss = list_possibilities(x_row)
    y_poss = list_possibilities(y_row)
    section_poss = list_possibilities(section)
    merged_list = x_poss + y_poss + section_poss
    possibilities = [item for item, count in collections.Counter(merged_list).items() if count == 3]
    return possibilities
