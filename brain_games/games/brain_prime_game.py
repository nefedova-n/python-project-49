from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round():
    random_number = randint(2, 1000)
    question = str(random_number)
    correct_answer = ''
    if random_number % 2 == 0:
        correct_answer = 'no'
    else:
        div_random_number = random_number // 2
        while div_random_number > 1:
            if random_number % div_random_number == 0:
                correct_answer = 'no'
                break
            else:
                div_random_number -= 1
            correct_answer = 'yes'
    return question, correct_answer