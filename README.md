# Word Guessing Game

This simple Python application features a game where the user has to guess a word. The game is built around guessing the letters of a randomly selected word. 
The user is given 10 lives, and these lives decrease with incorrect guesses.

## Usage

To start the game, navigate to the terminal or command prompt and run the following command:

```bash
python word_guess_game.py
```

When the game starts, the user is prompted to enter a name. After entering a valid name, the game begins, and the user is given 10 lives. 
The user tries to guess the letters of a randomly selected word. For each correct guess, the corresponding letter of the word is revealed. With each incorrect guess, the user loses a life.

## Rules
The user's name should consist only of letters and must be at least 3 characters long.
Word guesses can only be a single letter and cannot include spaces.

## Example Gameplay
```bash
Please enter your name: John
Hello John, Let's start the game
You have 10 lives
-
-
-
-
-
-
Enter your guess: a
You have left 9

-
-
-
-
-
-
Enter your guess: e
e
-
-
-
e
-
Enter your guess: k
e
-
-
k
e
-
Enter your guess: l
e
l
l
k
e
-
Enter your guess: o
e
l
l
k
e
o
!!! Congratulations John, You won !!!
```

## Requirements
Python 3.x

## Notes
Enjoy playing your game!
You can customize the game by adding more words or modifying the code, such as updating the words list.
To exit the game, you can use the Ctrl+C combination.
