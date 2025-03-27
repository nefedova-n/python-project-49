from random import randint

import prompt


def even_game(): 

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    success = 0
    while count < 3:
        random_number = randint(1, 10)
        result = ''        
        if random_number % 2 == 0:
            result = 'yes'
        else: 
            result = 'no'    
        print("Question: " + str(random_number))
        answer = prompt.string("Your answer: ") 
        if answer != result:
            print("'" + answer + "'" + " is wrong answer ;(.")
            print("Correct answer was " + "'" + result + "'")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
            count += 1
            success += 1        
    if success == 3:
        print("Congratulations, " + name + "!") 