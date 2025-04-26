from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def get_round():
    random_number = randint(1, 90)
    question = str(random_number)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer