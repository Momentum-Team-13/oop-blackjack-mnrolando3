- Write classes in Python, and determine appropriate attributes for those classes.
    - Classes: Human, Dealer, Card, Deck
        - Deck is a list of all card instances that are subtracted when method Deal is called
        - Card with suits, ranks, points as constants
        - Human has hand as attribute; hand is a list of card instances that get added when method Deal is called
        - Dealer has hand as attribute; hand is a list of card instances that get added when method Deal is called
- Objective to have a hand of cards whose sum is as close to 21 as possible without going over. 
    - Two players: dealer (computer) and human.
        Dealer
        - need to have hand (list to store dealt cards)
        - sum cards in hand
        - loop to draw cards and append to list while sum is less than 17
        - stop when sum is 17 or more and turn goes to Human
        - win if sum = 21
        Human
        - need to have hand (list to store dealt cards)
        - sum cards in hand
        - loop to draw cards and append to list while sum is less than 21
        - lose if over 21
        - ability to stay, then turn goes back to Dealer
        - win if sum = 21
- Write methods appropriate to each class.
    - Deal
        - Belongs to Dealer and Deck
        - select 2 random choice of Deck (dictionary of cards) and adds to Dealer hand and subtracts from Deck
        - select 2 random choice of updated Deck (dictionary of cards) and add
    - Hit/Draw
        - Belongs to Dealer, Human, and Deck
        - select
    - Stay(?)
    - Shuffle
        - Belongs to Dealer and Deck
    - Sum
        - Belongs to Dealer and Human
    - Ace
        - Belongs to Dealer and Human(?)



## Reqirements
- Build a blackjack game using python between a player and a dealer. 
    - The deck is shuffled, and the dealer and player are dealt 2 cards.  
    - The dealer's play is dictated by the rules of the game, and the dealer goes first. The dealer "hits" (is dealt a card) until their hand total is 17 or greater, at which point they stay. The dealers cards are all visible to the player.
    - The player then chooses whether to hit (be dealt a card) or stay. The player may hit as many times as they want before staying, but if their hand totals over 21, they "bust" and lose. 
    - If you want to make the game work for multiple players, go for it.
    - The deck is a standard 52 card deck with 4 suits. Face cards are worth 10. The Ace card can be worth 1 or 11. 
        - SUITS = Hearts, Diamonds, Spades, Clubs
        - RANKS = A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
- Use classes. One way to think about classes is that they are the _nouns_ involved in what you are modeling, so Card, Deck, Player, Dealer, and Game are all nouns that could be classes.
- Give those classes methods. Think about the _actions_ that happen to or are caused by these different elements. These choices are subjective and hard, and there is no one right way.
- Use your classes and methods to execute the gameplay. It is always a great idea to sketch and/or comment this out first before writing code.

## Optional items once your game works
- Keep track of total wins over multiple games.
- Introduce betting.
- Try an automated non-dealer player and figure out how you dictate their behavior.
- Make your program [count cards](https://en.wikipedia.org/wiki/Card_counting). Note this gets you kicked out of casinos.
