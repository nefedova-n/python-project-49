import random

DESCRIPTION = 'What is the result of the expression?'


def get_round(): 
    sub = " - "
    sum = " + "
    mult = " * "
    int_one = random.randint(1, 10)
    int_two = random.randint(1, 10)
    list = [sub, sum, mult]
    random.shuffle(list)
    random_expression = random.choice(list)
    question = str(int_one) + random_expression + str(int_two)
    correct_answer = eval(question)
    return question, correct_answer