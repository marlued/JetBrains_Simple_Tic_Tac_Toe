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


def check_for_draw(grid, game_won):
    list_of_fields = [value for value in grid.values()]
    return len([item for item in list_of_fields if item == '_']) == 0 and \
           game_won is False


def set_value(grid, field, turn):
    for key, value in grid.items():

        if key == field and (value == 'X' or value == 'O'):
            return False

        if key == field and (value != 'X' and value != 'O'):
            grid[key] = turn

    return grid
