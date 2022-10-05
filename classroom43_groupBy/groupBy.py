"""

GroupBy

"""

# tee - é utilizado para fazer copias
from itertools import groupby, tee

students = [
    {'name': 'Luiz', 'note': 'A'},
    {'name': 'Leticia', 'note': 'B'},
    {'name': 'Fabricio', 'note': 'A'},
    {'name': 'Rosemary', 'note': 'C'},
    {'name': 'Joana', 'note': 'D'},
    {'name': 'Jão', 'note': 'A'},
    {'name': 'Eduardo', 'note': 'B'},
    {'name': 'André', 'note': 'A'},
    {'name': 'Anderson', 'note': 'C'},
    {'name': 'José', 'note': 'B'},
]

sort_lambda_function = lambda item: item['note']

students.sort(key=sort_lambda_function)
grouped_students = groupby(students, sort_lambda_function)

print('Students sorted by note')
for student in students:
    print(student)

print()
print('Students grouped by note')
for grouping, student_iter in grouped_students:
    """
    Usamos o tee() para fazer uma copia de student_iter que por sua vez é um iterable
    isso significa que ao utilizado em algum for ou qualquer função que irá passar
    item a item dentro dele (iteração), cada item sera removido/descartado de dentro do
    iterable.
    """
    students_data_copy_1, students_data_copy_2 = tee(student_iter)

    print(f'Grouping: {grouping}')

    quantity_students_of_grouping = len(list(students_data_copy_1))

    print(f'Quantity students with Note {grouping}: {quantity_students_of_grouping}')

    for student_data in students_data_copy_2:
        print(f'\t{student_data}')

    print()
