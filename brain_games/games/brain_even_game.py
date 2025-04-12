from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    result = '' 
    if number % 2 == 0:
        result = 'yes'
    else: 
        result = 'no'
    return result


def get_round():
    random_number = randint(1, 10)
    question = str(random_number)
    correct_answer = is_even(random_number)
    return question, correct_answer