from random import choice
import os

def clearScreen():
    # for windows
    if os.name == "nt":
        _= os.system("cls")
    # for other os
    else:
        _= os.system("clear")

while True:
    try:
        userName = input("Please enter your name: ")
        if not userName.replace(" ", "").isalpha() or len(userName) <= 2:
            raise ValueError("Username must contain only letters and cannot be less than 3 characters.")
        
        clearScreen()
        print(f"Hello {userName}, Let's start the game")
        print("You have 10 lives")
        break  
    except ValueError as E:
        print(E)


words = ["metallica", "shakira", "sagopakajmer", "keylogger"]
secretWord = choice(words)
lives = 10
guessWords = ""
allGuess = set()

while lives > 0:   
    characterLeft = 0 
    for character in secretWord:
        if character in guessWords:
            print(character)
        else:
            print("-")
            characterLeft += 1

    if characterLeft == 0:
        clearScreen()
        print(secretWord)
        print(f"!!! Congratulations {userName}, You won !!!")
        break

    try:
        guess = input("Enter your guess: ")
        if len(guess) > 1 or not guess.replace(" ", "").isalpha():
            raise ValueError("Word cannot more than 1")
        else:
            guessWords += guess
            if guess not in secretWord:
                lives -=1
                print(f"You have left {lives}")
    except ValueError as e:
        print(e)

    print()

    if lives == 0:
        clearScreen()
        print("You lost")
        print(f"Secret word was '{secretWord}'")
    
    