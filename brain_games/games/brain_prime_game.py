from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    result = ''
    if number % 2 == 0:
        result = 'no'
    else:
        div_number = number // 2
        while div_number > 1:
            if number % div_number == 0:
                result = 'no'
                break
            else:
                div_number -= 1
            result = 'yes'
    return result


def get_round():
    random_number = randint(2, 1000)
    question = str(random_number)
    correct_answer = is_prime(random_number)
    return question, correct_answer