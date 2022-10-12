from crud_actions import add_task, show_tasks, do_undo, do_redo


def choose_action(option, task_list, redo_list):
    # adding a task
    if option == 1:
        return add_task(task_list)

    # showing task list
    if option == 2:
        show_tasks(task_list)

    # undo
    if option == 3:
        do_undo(redo_list, task_list)

    # redo
    if option == 4:
        try:
            do_redo(redo_list, task_list)

        except ValueError as error:
            print(f'An error has occurred - {error}')

    # exit
    if option == 5:
        exit()
