class Dealer():
    def __init__(self):
        self.dealer_hand = []
        pass

    # randomly selects 2 cards from Deck and adds to player_hand
    # 2 cards selected are removed from Deck
    # randomly selects 2 cards from Deck and adds to dealer_hand
    # 2 cards selected are removed from Deck
    def start_deal(self):
        pass

    # while loop as long as sum of dealer_hand < 17
    # randomly select 1 card from Deck and add to dealer_hand
    # card selected is removed from Deck
    # when sum of dealer_hand >= 17, stop
    def hit_dealer(self):
        pass

    def dealer_score():
        pass


# for player
class Player():
    def __init__(self):
        self.player_hand = []
        pass
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

# other methods:
# Ace (11 vs 1 value)
# do we want the Ace value as a method for the Dealer/Player classes
# or for the Card class?
