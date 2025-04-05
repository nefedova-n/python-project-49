import math
from random import randint

import prompt


def gcd_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")    
    print("Hello, " + name + "!")
    print("Find the greatest common divisor of given numbers.")
    count = 0
    success = 0
    while count < 3:
        int_one = randint(1, 10)
        int_two = randint(1, 100)
        result = math.gcd(int_one, int_two)
        integers = str(int_one) + " " + str(int_two)
        print("Question: " + integers)
        answer = prompt.string("Your answer: ")
        if answer != str(result):
            print("'" + answer + "'" + " is wrong answer ;(.")
            print("Correct answer was " + "'" + str(result) + "'")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
            count += 1
            success += 1        
    if success == 3:
        print("Congratulations, " + name + "!") 