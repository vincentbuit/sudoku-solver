from find_sections import find_sections
from find_y import find_y
from print_sudoku import print_sudoku
from sudoku_input import sudoku_start
from is_solved import is_solved
import collections
from remake_sudoku import remake_sudoku
from update_possibilities_matrix import update_possibilities_matrix

def solve_sudoku():
    # Remake the sudoku due to the object reference (we can't say sudoku_current = sudoku start)
    sudoku_current = remake_sudoku(sudoku_start)
    print('\nThe solution to the sudoku is:\n')
    # While the sudoku remains unsolved we continue our loop
    while is_solved(sudoku_current) is False:
        # Update possibilities matrix
        possibilities_matrix = update_possibilities_matrix(sudoku_current)
        # Get possibilities from an y_row and sections perspective
        y_rows_poss = find_y(possibilities_matrix)
        sections_poss = find_sections(possibilities_matrix)
        # Create one list for each in order to find the numbers which occur only 1 time
        for i in range(0, 9):
            all_y_row = []
            all_x_row = []
            all_sections = []
            for p in range(0, 9):
                if y_rows_poss[i][p][0] is not None and len(y_rows_poss[i][p]) != 0:
                    all_y_row = all_y_row + y_rows_poss[i][p]
                if possibilities_matrix[i][p][0] is not None and len(possibilities_matrix[i][p]) != 0:
                    all_x_row = all_x_row + possibilities_matrix[i][p]
                if sections_poss[i][p][0] is not None and len(sections_poss[i][p]) != 0:
                    all_sections = all_sections + sections_poss[i][p]
            single_occurence_y = [item for item, count in collections.Counter(all_y_row).items() if count == 1]
            single_occurence_x = [item for item, count in collections.Counter(all_x_row).items() if count == 1]
            single_occurence_section = [item for item, count in collections.Counter(all_sections).items() if count == 1]
            # Find the fields corresponding to the numbers found
            for j in range(0, len(single_occurence_y)):
                for k in range(0, 9):
                    if single_occurence_y[j] in y_rows_poss[i][k]:
                        sudoku_current[k][i] = single_occurence_y[j]
                        break
            for l in range(0, len(single_occurence_x)):
                for m in range(0, 9):
                    if single_occurence_x[l] in possibilities_matrix[i][m]:
                        sudoku_current[i][m] = single_occurence_x[l]
                        break
            for n in range(0, len(single_occurence_section)):
                for o in range(0, 9):
                    if single_occurence_section[n] in sections_poss[i][o]:
                        if i == 0:
                            if 0 <= o <= 2:
                                sudoku_current[0][o] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[1][o - 3] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[2][o - 6] = single_occurence_section[n]
                            break
                        elif i == 1:
                            if 0 <= o <= 2:
                                sudoku_current[0][o + 3] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[1][o] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[2][o - 3] = single_occurence_section[n]
                            break
                        elif i == 2:
                            if 0 <= o <= 2:
                                sudoku_current[0][o + 6] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[1][o + 3] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[2][o] = single_occurence_section[n]
                            break
                        elif i == 3:
                            if 0 <= o <= 2:
                                sudoku_current[3][o] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[4][o - 3] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[5][o - 6] = single_occurence_section[n]
                            break
                        elif i == 4:
                            if 0 <= o <= 2:
                                sudoku_current[3][o + 3] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[4][o] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[5][o - 3] = single_occurence_section[n]
                            break
                        elif i == 5:
                            if 0 <= o <= 2:
                                sudoku_current[3][o + 6] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[4][o + 3] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[5][o] = single_occurence_section[n]
                            break
                        elif i == 6:
                            if 0 <= o <= 2:
                                sudoku_current[6][o] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[7][o - 3] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[8][o - 6] = single_occurence_section[n]
                            break
                        elif i == 7:
                            if 0 <= o <= 2:
                                sudoku_current[6][o + 3] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[7][o] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[8][o - 3] = single_occurence_section[n]
                            break
                        elif i == 8:
                            if 0 <= o <= 2:
                                sudoku_current[6][o + 6] = single_occurence_section[n]
                            elif 3 <= o <= 5:
                                sudoku_current[7][o + 3] = single_occurence_section[n]
                            elif 6 <= o <= 8:
                                sudoku_current[8][o] = single_occurence_section[n]
                            break
        # Debug purposes
        #print_sudoku(sudoku_current)
        #print('\n\n\n')
    print_sudoku(sudoku_current)


solve_sudoku()
