"""
Faça uma lista de tarefas com as seguintes opções:

    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

"""

from menu_components import menu
from action_components import choose_action

print('-------- To do --------')

start = True
task_list = []
redo_list = []

while start:
    option = menu()

    last_task = choose_action(option, task_list, redo_list)
