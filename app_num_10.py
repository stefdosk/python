from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
par_deck = []

player1 = []
player2 = []
player1_score = 0
player2_score = 0


class Card(IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class Suit(Enum):
    Spades = 'Spades'
    Hearts = 'Hearts'
    Clubs = 'Clubs'
    Diamonds = 'Diamonds'


class Poker:
    def __init__(self, card_num, card_suit):
        self.card = card_num
        self.suit = card_suit


def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(Poker(Card(card), Suit(suit)))
    return full_deck


def draw_card(deck):
    rand_card = randint(0, len(deck) - 1)
    return deck.pop(rand_card)


def deal_hand():
    for i in range(0, 5):
        player1.append(draw_card(partial_deck))
        player2.append(draw_card(partial_deck))


def five_of_a_kind():
    foak1 = False
    foak2 = False
    if player1[0].card == player1[1].card == player1[2].card == player1[3].card == player1[4].card:
        player1_score = 6
        foak1 = True
    if player2[0].card == player2[1].card == player2[2].card == player2[3].card == player2[4].card:
        player2_score = 6
        foak2 = True
    if foak1 == True and foak2 == True:
        for i in range(0, 5):
            if player1[i].card > player2[i].card:
                print("Ο παίκτης 1 κέρδισε!")
                break
            elif player1[i].card < player2[i].card:
                print("Ο παίκτης 2 κέρδισε!")
                break
            else:
                i += 1


create_deck()
partial_deck = list(full_deck)
deal_hand()
five_of_a_kind()
