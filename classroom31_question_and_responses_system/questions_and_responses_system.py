"""

Questions and Answer System

"""

questions = {
    'Question 1': {
        'question': 'How much is 2 + 2 ?',
        'responses': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'correct_response': 'b',
    },
    'Question 2': {
        'question': 'How much is 5 * 5 ?',
        'responses': {
            'a': 25,
            'b': 50,
            'c': 5,
        },
        'correct_response': 'a',
    }
}
print()

corrected_answers_counter = 0
wrong_answers_counter = 0

for question_key, question_value in questions.items():
    print(f'{question_key}: {question_value.get("question")}')

    print('Choose your response below: ')

    for response_key, response_value in question_value.get('responses').items():
        print(f'{response_key}: {response_value}')

    print()
    user_response = input("What your response ? - ")

    if user_response == question_value.get('correct_response'):
        corrected_answers_counter += 1
        print('Congratulations, you are corrected!')
    else:
        wrong_answers_counter += 1
        print('\tWell, you are wrong!, the correct answer is letter b, try again!')

    print()

print()
print('Ranking:\n')
print(f'\tCorrected Answers: {corrected_answers_counter}')
print(f'\tWrong Answers: {wrong_answers_counter}')

quantity_questions = len(questions)
correct_percent = corrected_answers_counter / quantity_questions * 100

print(f'Your hit percent was {correct_percent:.0f} %')
