'''              This is code for Hangman game.

    In this game, there is a list of words present,
    out of which our interpreter will choose 1 random word.
    The user first has to input their names and then,
    will be asked to guess any alphabet. 
    If the random word contains that alphabet,
    it will be shown as the output(with correct placement)
    else the program will ask you to guess another alphabet.
    User will be given 12 turns(can be changed accordingly)
    to guess the complete word.
'''

import random

def play_game(words):
    
    name = input("Enter your name : ")
    print("Welcome to the Hangman-Game",name)
    word = list(words)
    attempts = 6
    board = ["_"]*len(word)
    win = False
    print(display_hangman(attempts))
    print(board)
    while attempts > 0:
        guess = input("Guess the character!!!")
        if guess in word:
            ind = word.index(guess)
            board[ind] = guess
            word[ind] = '$'
        else:
            attempts -= 1
            
        print(display_hangman(attempts))
        print(board)

        if "_" not in board:
            print("Congratulations!!!")
            print("You have guessed the word ",end="")
            print("".join(board),end="")
            win = True
            break
        
    if not win:
        print("You lose the game")
        print ("the word will be ",end="")
        print("".join(words))
    

def display_hangman(attempts):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
                   
    ]
    return stages[attempts]

if __name__ == '__main__':
    
    word_list = ['cat','star','fever','reba']
    words = random.choice(word_list)
    play_game(words)
    
