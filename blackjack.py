# Write your blackjack game here.

# for player
class Player():
    def __init__(self):
        self.player_hand = []
    # right? that makes sense? Yes i believe so

    # ask for another card
    def hit_player(self):
        pass

    # calculate score
    def player_score():
        pass
    
    # this feels spicy -Diego
    # betting is in our "extras" haha
    def place_wager():
        pass


class Deck():
    def __init__(self):
        self.cards = []
        pass

    def __str__(self):
        for card in self.cards:
            print('this is card in Deck', self.cards)
            return f"this should be our card {self.cards}"

    def print_cards(self):
        # print('CARDSS', self.cards)
        for card in self.cards:
            # print(self.cards)
            print('this is card in Deck', len(self.cards))
            return f"this should be our card {card}"
        # create cards and add to list

    def add_cards(self, card):
        self.cards.append(card)
        pass

    # random function. random.choice
    def shuffle_cards():
        pass

# so this whole thing can be a list?
# an attribute within the deck class?
# yeah I think so, the list attribute will contain many instances of the card class 52 I believe 
# do we need a separate class for Cards, then? Will we be able to extract the individual instances for each card without having a separate card class? Will our deck code be too bulky if we do that?
# that is right, didn't think about that...
class Card():
    def __init__(self, suit, value, rank):
        # card rank (face/number)
        self.rank = rank
        # card suit
        self.suit = suit
        # card point value
        self.value = value
        pass


    def __str__(self):
        return f"{self.value} {self.suit} {self.rank}"
    
    # add cards to deck -> should this be part of the deck class? yeah, I think that makes more sense
    # def add_to_deck(self):
    #   pass


# is this redundant? no because the Dealer needs 
# to start the deal and has different rules than a player 
# (loop will stop at 17, etc)
class Dealer():
    def __init__(self):
        self.dealer_hand = []

    # randomly selects 2 cards from Deck and adds to player_hand
    # 2 cards selected are removed from Deck
    # randomly selects 2 cards from Deck and adds to dealer_hand
    # 2 cards selected are removed from Deck
    def start_deal(self):
        pass

    # while loop as long as sum of dealer_hand < 17
    # randomlly select 1 card from Deck and add to dealer_hand
    # card selected is removed from Deck
    # when sum of dealer_hand >= 17, stop
    def hit_dealer(self):
        pass

    def dealer_score():
        pass


# other methods:
# Ace (11 vs 1 value)
# do we want the Ace value as a method for the Dealer/Player classes or for the Card class?
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
print("deck.print_cards", deck.print_cards())