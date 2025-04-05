from random import randint

import prompt


def prime_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")    
    print("Hello, " + name + "!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    success = 0
    while count < 3:
        random_number = randint(2, 1000)
        result = ''
        if random_number % 2 == 0:
            result = 'no'
        else:
            div_random_number = random_number // 2
            while div_random_number > 1:
                if random_number % div_random_number == 0:
                    result = 'no'
                    break
                else:
                    div_random_number -= 1
                result = 'yes'
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