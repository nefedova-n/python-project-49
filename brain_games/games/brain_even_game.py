from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    random_number = randint(1, 10)
    question = str(random_number)
    correct_answer = ''        
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else: 
        correct_answer = 'no'
    return question, correct_answer