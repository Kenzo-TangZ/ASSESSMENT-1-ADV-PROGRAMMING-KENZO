import random
from random import randint, choice

def displayMenu():
    print("Choose Math quiz difficulty: \n" \
    "[1] Easy\n" \
    "[2] Medium\n" \
    "[3] Hard")
    
    Difficulty = str(input("Choose Math Quiz Difficulty (Easy-Hard): ").lower())
    while Difficulty not in ("easy", "medium", "hard"):
        print("Not in the diffficulties given, try again.")
        Difficulty = str(input("Choose Math Quiz Difficulty (Easy-Hard): ").lower())
    return Difficulty

def randomInt(Difficulty):
    if Difficulty == "easy":
        return randint(1,9)
    elif Difficulty == "medium":
        return randint(10, 99) 
    else:
        return randint(1000, 9999) 
    
def decideOperation():
    return choice(["+", "-"])

def decideProblem (Num1, operation, Num2):
    while True:
        try:
            return int(input(f"What is {Num1} {operation} {Num2}? "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def isCorrect(Answer, CorrectAns, Attempt):
    if Answer == CorrectAns:
        if Attempt == 1:
            print("Your answer is correct (10 points awarded)")
            return 10
        else:
            print("Your answer is correct (5 points awarded)")
            return 5    
    else:
        print("That is the wrong answer")
        return 0    

def displayResutlts(finalScore):
    if finalScore >= 90:
        grade = "A+"
    elif finalScore >= 85:
        grade = "A"
    elif finalScore >= 80:
        grade = "A-"
    elif finalScore >= 75:
        grade = "B+"
    elif finalScore >= 70:
        grade = "B"
    elif finalScore >= 65:  
        grade = "B-"
    elif finalScore >= 60:
        grade = "C"
    elif finalScore >= 55:
        grade = "D"
    else: 
        grade = "F"
    
    print(f"\n Score = {finalScore}/100 \n Grade: {grade}")

def MathsQuiz():
    while True:
        Diff = displayMenu()
        points = 0

        for q_num in range (1, 11):
            Num1 = randomInt(Diff)
            Num2 = randomInt(Diff)
            Operation = decideOperation()

            if Operation == "-" and Num2 > Num1:
                Num1, Num2 = Num2, Num1

            cor = Num1 + Num2 if Operation == "+" else Num1 - Num2

            print(f"\nQ {q_num}: ")
            
            score_earned = 0
            
            Answer = decideProblem(Num1, Operation, Num2)
            score_earned = isCorrect(Answer, cor, 1)

            if score_earned == 0:
                print("You have one attempt left.")
                Answer = decideProblem(Num1, Operation, Num2)
                score_earned = isCorrect(Answer, cor, 2)
            
            points += score_earned
            print(f"Current Score: {points}")

        displayResutlts(points)
    
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye.")
            break 

MathsQuiz()