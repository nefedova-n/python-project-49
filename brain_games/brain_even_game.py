from random import randint
from cli import welcome_user

def even_game(): 
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    success = 0
    while count < 3:
        random_number = randint(1, 20)
        result = ''        
        if random_number % 2 == 0:
            result = 'yes'
        else: 
            result = 'no'    
        print("Question: " + str(random_number))
        answer = ''
        while answer == '':
            print("Your answer: ", end='')
            answer = input()       
        if answer != result:
            print("'" + answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + result + "'")
            print("Let's try again, " + "name" + "!")
            break
        else:
            print('Correct!')
            count += 1
            success += 1
        
    if success == 3:
        print("Congratulations " + "name" + "!") 

welcome_user()
even_game()