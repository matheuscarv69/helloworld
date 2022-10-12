def add_task(task_list):
    task = input('Enter your task: ')

    task_list.append(task)

    return task


def show_tasks(task_list):
    print()

    if not len(task_list) == 0:
        print(f'Show tasks')

        for key, task in enumerate(task_list, start=1):
            print(f'\t {key} - {task}')
    else:
        print('Task list is empty')


def do_undo(redo_list, task_list):
    last_task = task_list.pop()
    redo_list.append(last_task)


def do_redo(redo_list, task_list):
    if len(redo_list) == 0:
        raise ValueError('Nothing to redo.')

    last_task = redo_list.pop()
    task_list.append(last_task)
