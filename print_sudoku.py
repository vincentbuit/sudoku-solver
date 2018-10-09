from colorama import Fore
from sudoku_input import sudoku_start


def print_sudoku(sudoku_current):
    color_matrix = {'border': Fore.BLUE, 'start': Fore.RED, 'solved': Fore.GREEN}
    for y in range(0, 9):
        row = ''
        if y == 3 or y == 6:
            print('{color_matrix[border]} -------- + --------- + --------\n'.format(color_matrix=color_matrix))
        for x in range(0, 9):
            if x == 3 or x == 6:
                row += '{color_matrix[border]} | '.format(color_matrix=color_matrix)
            if sudoku_current[y][x] == 0:
                row += ('   ')
            elif sudoku_start[y][x] != 0:
                row += '{color_matrix[start]} '.format(color_matrix=color_matrix) + (
                    str(sudoku_current[y][x])) + ' '
            else:
                row += '{color_matrix[solved]} '.format(color_matrix=color_matrix) + (
                    str(sudoku_current[y][x])) + ' '
        print(row + '\n')
