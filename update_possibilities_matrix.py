from find_possibilities import find_possibilities


def update_possibilities_matrix(sudoku_current):
    y_coordinates_updated = []
    x_coordinates_updated = []
    possibilities_matrix = []
    for y in range(0, 9):
        row_list = []
        for x in range(0, 9):
            if sudoku_current[y][x] == 0:
                current_field_poss = find_possibilities(y, x, sudoku_current)
                # Fill in field if only 1 possibility
                if len(current_field_poss) == 1:
                    sudoku_current[y][x] = current_field_poss[0]
                    y_coordinates_updated.append(y)
                    x_coordinates_updated.append(x)
                    row_list.append([None])
                else:
                    row_list.append(current_field_poss)
            else:
                row_list.append([None])
        possibilities_matrix.append(row_list)
    # Update possibilities matrix based on fresh filled in fields
    for q in list(set(y_coordinates_updated)):
        for r in range(0, 9):
            if sudoku_current[q][r] == 0:
                current_field_poss = find_possibilities(q, r, sudoku_current)
                possibilities_matrix[q][r] = current_field_poss
            else:
                possibilities_matrix[q][r] = [None]
    for s in list(set(x_coordinates_updated)):
        for t in range(0, 9):
            if sudoku_current[t][s] == 0:
                current_field_poss = find_possibilities(t, s, sudoku_current)
                possibilities_matrix[t][s] = current_field_poss
            else:
                possibilities_matrix[t][s] = [None]
    return possibilities_matrix
