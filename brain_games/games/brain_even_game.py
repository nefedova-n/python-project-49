from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def create_number():
    random_number = randint(1, 10)
    return random_number

def check_answer(random_number):
    correct_answer = ''        
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else: 
        correct_answer = 'no'
    return correct_answer

def get_round():
    random_number = create_number()
    question = str(random_number)
    return question, check_answer(random_number)