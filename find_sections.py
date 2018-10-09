# Takes a list of sudoku's, returns a list of lists 9 square sections
def find_sections(sudoku):
    sections = []
    lower = 0
    upper = 3
    while len(sections) != 9:
        new_section_1 = []
        new_section_2 = []
        new_section_3 = []
        for y in range(lower, upper):
            for x1 in range(0, 3):
                new_section_1.append(sudoku[y][x1])
            for x2 in range(3, 6):
                new_section_2.append(sudoku[y][x2])
            for x3 in range(6, 9):
                new_section_3.append(sudoku[y][x3])
        sections.append(new_section_1)
        sections.append(new_section_2)
        sections.append(new_section_3)
        lower += 3
        upper += 3
    return sections
