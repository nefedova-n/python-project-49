from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return False
    div_number = number // 2
    while div_number > 1:
        if number % div_number == 0:
            return False
        else:
            div_number -= 1
    return True 


def get_round():
    random_number = randint(3, 1000)
    question = str(random_number)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer