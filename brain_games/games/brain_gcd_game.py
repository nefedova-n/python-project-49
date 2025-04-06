import math
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round():
    int_one = randint(1, 10)
    int_two = randint(1, 100)
    correct_answer = str(math.gcd(int_one, int_two))
    question = str(int_one) + " " + str(int_two)
    return question, correct_answer