#!/usr/bin/python
#-*- coding: utf-8 -*-
cards = input("Enter list of your cards: ")


def blackjack(cards):
    result = 0
    a_count = 0
    dictionary = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }
    for card in cards.split():
        if card in dictionary:
            result = result + dictionary[card]
        elif card == 'A':
            a_count = a_count + 1

    if a_count > 0:
        for i in range(a_count):
            if a_count > 1:
                result = result + 1
                a_count = a_count - 1
            else:
                if result + 11 < 22:
                    result = result + 11
                else:
                    result = result + 1

    if result <= 21:
        return result
    else:
        return 'Bust'



print(blackjack(cards))
