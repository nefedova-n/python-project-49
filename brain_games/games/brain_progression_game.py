from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def replace_number_in_list(list):
    count = 0
    n = 1
    margin = randint(1, 4)
    n_random = randint(1, 10)
    while count < 10:
        list.append(list[n - 1] + margin)
        count += 1
        n += 1
    change_int = list[n_random]
    list[n_random] = '..'    
    result = ' '.join(map(str, list))
    return change_int, result


def get_round():
    list = []
    first_int = randint(1, 10)
    list.append(first_int)
    change_int, result = replace_number_in_list(list)
    question = str(result)
    correct_answer = str(change_int)
    return question, correct_answer