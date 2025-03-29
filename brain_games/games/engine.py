import prompt


def engine_greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")    
    print("Hello, " + name + "!")