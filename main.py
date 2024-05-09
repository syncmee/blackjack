import random

import math

import os

from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
computers_cards = [] 
n_score = 0
n_score_computer= 0
my_score = 0
computers_score = 0 
end_game = False
reference = 21
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


def closer_to_reference(reference, my_score, computers_score):
    global end_game
    diff1 = (reference - my_score)
    diff2 = (reference - computers_score)

    if diff1 < diff2 and my_score < 21:
        print("You win")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True
    elif diff2 < diff1 and computers_score < 21:
        print("You Lose")
        print(f"Your final hand: {my_cards}, current score: {my_score}")
        print(f"Computer's final hand: {computers_cards}, computers score {computers_score}")
        end_game = True

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
                closer_to_reference(reference, my_score, computers_score)
                
            
    else:
        end_game = True