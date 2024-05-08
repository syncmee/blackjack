import random

import math

import os

from art import logo

end_game = False
def scorecheck():
    global end_game
    if my_score > 21:
        print("You Lose")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True
    elif computers_score > 21:
        print("You win")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True
    elif my_score == 21: 
        print("You won!")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True
    elif computers_score == 21:
        print("You Lose")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True
        
def scoreadd():
    global my_score
    global computers_score
    for n in my_cards:
        my_score += n
    for m in computers_cards:   
        computers_score += m

def scorecheck_n():
    global end_game
    n_score = 21 - my_score
    n_score_computer = 21 - computers_score
    if n_score > n_score_computer: 
        print("You won!")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True
    elif n_score_computer > n_score:
        print("You Lose")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
computers_cards = [] 
n_score = 0
n_score_computer= 0
my_score = 0
computers_score = 0 
while not end_game:
    start_game = input("Do you want to play a game of black jack? Type 'y' or 'n': ")
    if start_game == "y":
        my_cards.append(random.choice(cards))
        my_cards.append(random.choice(cards))
        computers_cards.append(random.choice(cards))
        computers_cards.append(random.choice(cards))
        scoreadd()
        print(f"Your cards: {my_cards}, your score: {my_score}")
        print(f"Computer's first card: {computers_cards[0]}")
        scorecheck()
        while not end_game:
            continuegame = input("Type 'y' to get another card. Type 'n' to pass: ")
            if continuegame == "y":
                my_cards.append(random.choice(cards))
                computers_score = 0 
                my_score = 0
                scoreadd()
                print(f"Your cards: {my_cards}, your score: {my_score}")
                print(f"Computer's first card: {computers_cards[0]}")
                scorecheck()
                
            if continuegame == "n":
                computers_cards.append(random.choice(cards))
                computers_score = 0 
                my_score = 0
                scoreadd()
                scorecheck()
                scorecheck_n()
                
            
    else:
        end_game = True