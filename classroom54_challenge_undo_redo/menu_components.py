def menu():
    show_menu()

    try:
        option_selected = select_option()
        return option_selected
    except ValueError as error:
        print(f'An error has occurred - {error}')


def show_menu():
    print()
    print('Menu:')
    print('\t 1 - add task')
    print('\t 2 - show tasks')
    print('\t 3 - undo task')
    print('\t 4 - redo task')
    print('\t 5 - exit \n')


def select_option():
    option = int(input('Which an option: '))

    options_list = [1, 2, 3, 4, 5]

    if option not in options_list:
        raise ValueError(f'Selected option: {option} is invalid.')

    return option



