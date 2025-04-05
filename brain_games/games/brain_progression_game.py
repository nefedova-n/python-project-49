from random import randint

import prompt


def progression_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")    
    print("Hello, " + name + "!")
    print("What number is missing in the progression?")
    count = 0
    success = 0
    while count < 3:
        # герерируем последовательность
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
        # запускаем игру
        print("Question: " + result_output)
        answer = prompt.string("Your answer: ")
        if answer != str(change_int):
            print("'" + answer + "'" + " is wrong answer ;(.")
            print("Correct answer was " + "'" + str(change_int) + "'")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
            count += 1
            success += 1        
    if success == 3:
        print("Congratulations, " + name + "!")