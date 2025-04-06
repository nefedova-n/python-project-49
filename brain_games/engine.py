import prompt

COUNT_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print(game.DESCRIPTION)
    current_round = COUNT_ROUNDS
    success = 0
    while current_round > 0:
        question, correct_answer = game.get_round()
        print("Question: " + question)
        user_answer = prompt.string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again {name}!")
            break
        else:
            print('Correct!')
            current_round -= 1
            success += 1        
    if success == 3:
        print("Congratulations, " + name + "!") 