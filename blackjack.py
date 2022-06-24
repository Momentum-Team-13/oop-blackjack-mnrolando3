# Write your blackjack game here.


class Card():
    def __init__(self, rank, suit):
        # card rank (face/number)
        self.rank = rank
        # card point value
        self.value = None
        # card suit
        self.suit = suit
        # print(f'The {self.rank} of {self.suit} is {self.value} points.')

    def __str__(self):
        return f"{self.value} {self.suit} {self.rank}"

    # def add_to_deck(self):
    #     for suit_type in suit:
    #         for index in range(len(value)):
    #             value_type = value[index]
    #             rank_type = rank[index]
    #             name = f"{rank} {suit_type}"
    #             name = Card(suit_type, value_type, rank_type)
    #             return name
    #             deck.add_cards(name)


class Deck():
    def __init__(self):
        self.cards = []
        self.add_cards()
        # self.shuffle_cards()
        # print(f'deck? {self.cards}')

    def __str__(self):
        # for card in self.cards:
        # print('this is card in Deck', self.cards)
        return f"this should be our card {self.cards}"

    # def print_cards(self):
    #     # print('CARDSS', self.cards)
    #     for card in self.cards:
    #         # print(self.cards)
    #         print('print length of list', len(self.cards))
    #         return f"this is our deck {self.cards}"
    #     # create cards and add to list

    def add_cards(self):
        RANKS_VALUES = {'A':[1,11], '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
        SUITS = ['♠️', '♣️', '♥️', '♦️']

        for rank in RANKS_VALUES:
            # for value in RANKS_VALUES:
            for suit in SUITS:
                card = Card(rank, suit)
                self.cards.append(card)
                # print('print length of list', len(self.cards))
                # return f"this adds cards {self.cards}"

    # random function. random.choice
    def shuffle_cards():
        pass

deck = Deck()
deck.add_cards()

for card in deck.cards:
    print(card)
# suit = ['♠️', '♣️', '♥️', '♦️']
# value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# for suit_type in suit:
#     for index in range(len(value)):
#         value_type = value[index]
#         rank_type = rank[index]
#         name = f"{rank} {suit_type}"
#         name = Card(suit_type, value_type, rank_type)
#         # print(name)
# #         deck.add_cards(name)
#         deck.add_cards(name)

# print("deck.print_cards", deck.add_cards(name))
# print("deck.print_cards", deck.add_cards(name))
