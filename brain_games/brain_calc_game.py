import random

import prompt


def calc_game(): 
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")    
    print("Hello, " + name + "!")
    print("What is the result of the expression?")
    count = 0
    success = 0
    while count < 3:
        sub = " - "
        sum = " + "
        mult = " * "
        int_one = random.randint(1, 10)
        int_two = random.randint(1, 10)
        list = [sub, sum, mult]
        random.shuffle(list)
        random_expression = random.choice(list)
        expression = str(int_one) + random_expression + str(int_two)
        result = eval(expression)
        print("Question: " + expression)
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