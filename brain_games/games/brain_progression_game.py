from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_round():
    list = []
    first_int = randint(1, 10)
    margin = randint(1, 3)
    list.append(first_int)
    count_1 = 0
    n = 1
    n_random = randint(1, 9)
    while count_1 < 10:
        list.append(list[n - 1] + margin)
        count_1 += 1
        n += 1
    change_int = list[n_random]
    list[n_random] = '..'    
    result_output = ' '.join(map(str, list))
    question = str(result_output)
    correct_answer = str(change_int)
    return question, correct_answer