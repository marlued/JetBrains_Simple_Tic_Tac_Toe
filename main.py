# Definition of the required functions.

def print_field(grid):
    list_of_fields = [value for value in grid.values()]
    row_1 = list_of_fields[0:3]
    row_2 = list_of_fields[3:6]
    row_3 = list_of_fields[6:9]

    print('---------')
    print(f'| {" ".join(row_1)} |')
    print(f'| {" ".join(row_2)} |')
    print(f'| {" ".join(row_3)} |')
    print('---------')


def check_for_win(grid):
    list_of_fields = [value for value in grid.values()]

    if len([item for item in list_of_fields if item == '_']) == 9:
        return False
    if len(set(list_of_fields[0:3])) == 1:
        return True
    if len(set(list_of_fields[3:6])) == 1:
        return True
    if len(set(list_of_fields[6:9])) == 1:
        return True
    if len(set([list_of_fields[0], list_of_fields[4], list_of_fields[8]])) == 1:
        return True
    if len(set([list_of_fields[2], list_of_fields[4], list_of_fields[6]])) == 1:
        return True

    return False


def check_for_draw(grid, game_won_func):
    list_of_fields = [value for value in grid.values()]
    return len([item for item in list_of_fields if item == '_']) == 0 and \
           game_won_func is False


def set_value(grid, field, turn):
    for key, value in grid.items():

        if key == field and (value == 'X' or value == 'O'):
            return False

        if key == field and (value != 'X' and value != 'O'):
            grid[key] = turn

    return grid


# End of function definition.

# Initialization of the required variables

game_won = False
turn_of_player = 'X'
game_grid = {'1 1': '_',
             '1 2': '_',
             '1 3': '_',
             '2 1': '_',
             '2 2': '_',
             '2 3': '_',
             '3 1': '_',
             '3 2': '_',
             '3 3': '_'}

valid_coordinates = ['1 1', '1 2', '1 3',
                     '2 1', '2 2', '2 3',
                     '3 1', '3 2', '3 3']

# game loop

while game_won is not True:

    print_field(game_grid)
    user_input = input().strip()

    # exceptions

    try:
        if user_input.split()[0].isalpha() or user_input.split()[1].isalpha():
            raise ValueError('not a number')

    except ValueError:
        print('You should enter numbers!')
        continue

    try:
        if user_input not in valid_coordinates:
            raise IndexError('out of range')

    except IndexError:
        print('Coordinates should be from 1 to 3!')
        continue

    try:
        game_grid = set_value(game_grid, user_input, turn_of_player)

        if game_grid is False:
            raise ValueError('occupied')

    except ValueError:
        print('This cell is occupied! Choose another one!')
        continue

    # check if draw or win

    draw = check_for_draw(game_grid, check_for_win(game_grid))


    won = check_for_win(game_grid)

    print(draw, won)


    continue



