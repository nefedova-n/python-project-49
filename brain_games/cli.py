# import prompt


def welcome_user():
    
    # name = prompt.string('May I have your name? ')
    # print("Hello, " + name + "!")

    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
        print("Hello, " + name + "!")