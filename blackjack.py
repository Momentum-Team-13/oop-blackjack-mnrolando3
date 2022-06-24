# Write your blackjack game here.

class Deck():
    def __init__(self):
        self.cards = []

    # def __str__(self):
    #     for card in self.cards:
    #         print('this is card in Deck', self.cards)
    #         return f"this should be our card {self.cards}"

    # def print_cards(self):
    #     # print('CARDSS', self.cards)
    #     for card in self.cards:
    #         # print(self.cards)
    #         print('print length of list', len(self.cards))
    #         return f"this is our deck {self.cards}"
    #     # create cards and add to list

    def add_cards(self, card):
        self.cards.append(card)
        print('print length of list', len(self.cards))
        return f"this adds cards {self.cards}"

    # random function. random.choice
    def shuffle_cards():
        pass

# so this whole thing can be a list?
# an attribute within the deck class?
# yeah I think so, the list attribute will contain many instances of the card class 
# 52 I believe
# do we need a separate class for Cards, then?
# Will we be able to extract the individual instances for each card
# without having a separate card class? 
# Will our deck code be too bulky if we do that?
# that is right, didn't think about that...


class Card():
    def __init__(self, suit, value, rank):
        # card rank (face/number)
        self.rank = rank
        # card suit
        self.suit = suit
        # card point value
        self.value = value

    def __str__(self):
        return f"{self.value} {self.suit} {self.rank}"

    # add cards to deck -> should this be part of the deck class? 
    # yeah, I think that makes more sense
    # def add_to_deck(self):
    #     for suit_type in suit:
    #         for index in range(len(value)):
    #             value_type = value[index]
    #             rank_type = rank[index]
    #             name = f"{rank} {suit_type}"
    #             name = Card(suit_type, value_type, rank_type)
    #             return name
    #             deck.add_cards(name)


deck = Deck()
suit = ['♠️', '♣️', '♥️', '♦️']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for suit_type in suit:
    for index in range(len(value)):
        value_type = value[index]
        rank_type = rank[index]
        name = f"{rank} {suit_type}"
        name = Card(suit_type, value_type, rank_type)
        # print(name)
        deck.add_cards(name)

print("deck.print_cards", deck.add_cards(name))
