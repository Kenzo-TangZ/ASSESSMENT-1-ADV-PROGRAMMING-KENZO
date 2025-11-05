import random
import os

def readjokes(name):
    jokes = []
    with open(name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "?" in line:
                question, punchline = line.split("?", 1)
                jokes.append((question + "?", punchline.strip()))
    return jokes

def displayjoke(joke_list):
    print("\nOkay!")
    question, answer = random.choice(joke_list)
    print("\n" + question)
    input("Press Enter to display punchline...")
    print(answer + "\n")

def alexajokebot():
    jokespath = os.path.join(os.path.dirname(__file__), "jok.txt")
    alljokes = readjokes(jokespath)

    while True:
        user_input = input("Type 'Alexa tell me a joke' or 'quit' to leave: ").strip().lower()

        if user_input == "alexa tell me a joke":
            displayjoke(alljokes)
        elif user_input == "quit":
            print("Goodbye! Thanks for listening!")
            break
        else:
            print("\nPlease only type 'Alexa tell me a joke' or 'quit'.\n")

alexajokebot()