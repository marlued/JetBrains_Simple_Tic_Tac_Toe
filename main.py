# defining the necessary functions:

def build_structures(input_str, only_rows=False):
    # rows
    row_1 = list(input_str[0:3])
    row_2 = list(input_str[3:6])
    row_3 = list(input_str[6:9])

    # columns
    column_1 = list(input_str[0::3])
    column_2 = list(input_str[1::3])
    column_3 = list(input_str[2::3])

    # diagonals
    d_left = list(input_string[::4])
    d_right = list(input_string[2:7:2])

    # return values: only rows or everything
    if only_rows:
        return [row_1, row_2, row_3]

    else:
        return [row_1, row_2, row_3, column_1, column_2, column_3, d_left, d_right]


def print_grid(matrix_structure):
    print('---------')
    print(f'| {" ".join(matrix_structure[0])} |')
    print(f'| {" ".join(matrix_structure[1])} |')
    print(f'| {" ".join(matrix_structure[2])} |')
    print('---------')


def check_for_win(matrix_structure):
    win_x = any([element.count('X') == 3 for element in matrix_structure])
    win_o = any([element.count('O') == 3 for element in matrix_structure])

    # function returns 'impossible' if win_x and win_o are both True

    if win_x and win_o:
        return 'Impossible'

    if win_x:
        return 'X wins'
    if win_o:
        return 'O wins'


def check_for_draw(matrix_structure, func):
    # func -> call of function 'check_for_win', no other function possible

    empty_cells = any([item == '_' for element in matrix_structure
                       for item in element])

    if not empty_cells and func is None:
        print('Draw')


def check_for_impossible(matrix_structure):
    # case where both x and o wins is covered in function "check_for_win"

    all_elements = [item for element in matrix_structure for item in element]
    count_x = all_elements.count('X')
    count_o = all_elements.count('O')

    if count_x - count_o >= 2 or count_o - count_x >= 2:
        return 'Impossible'


def check_for_completion(matrix_structure, func):
    empty_cells = any([item == '_' for element in matrix_structure
                       for item in element])

    if empty_cells and func is None:
        return 'Game not finished'


# end of section where functions where defined.

input_string = input().strip()

# game_grid only contains the 3 rows but not all list items required for
# checking the conditions needed for check_for_win, check_for_draw and
# check_for_completion. It is used for printing the grid and for the function
# check_for_draw which requires only the three actual rows for the tests that
# are performed by this function

game_grid = build_structures(input_string, only_rows=True)

# all_conditions contains all possible conditions that have to be checked to
# determine if the game is won. This variable is therefore used for the
# following functions: check_for_win, check_for_draw and check_for_completion.
# It causes an error if it is used in the function check_for_impossible

all_conditions = build_structures(input_string, only_rows=False)

print_grid(game_grid)

if check_for_win(all_conditions):
    print(check_for_win(all_conditions))

if check_for_draw(all_conditions, check_for_win(all_conditions)):
    check_for_draw(all_conditions, check_for_win(all_conditions))

if check_for_impossible(game_grid):  # game_grid has to be used as argument!
    print(check_for_impossible(game_grid))

else:
    if check_for_completion(all_conditions, check_for_win(all_conditions)):
        print(check_for_completion(all_conditions, check_for_win(all_conditions)))
