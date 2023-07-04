```mermaid
classDiagram
    Game --> "*" Player : has
    Game --> "1" Deck : has
    Game --> "5" DiscardPile : has
    Game --> "*" Expedition : has
    Player --> "1" Hand : has
    Hand --> "*" Card : contains
    Player --> "*" Expedition : has
    Expedition --> "*" Card : contains
    AbstractPile <|-- Deck
    AbstractPile <|-- DiscardPile
    AbstractPile <|-- Hand
    class Game{
      #players
      #deck
      #discardPiles
      #expeditions
      #currentPlayer
      +start()
      +end()
      +calculateScores()
      +turn(Player)
    }
    class Player{
      #name
      #hand
      #expeditions
      +playCard(Card, Expedition)
      +discardCard(Card, DiscardPile)
      +drawCard(AbstractPile)
      +selectCard() : Card
    }
    class AbstractPile{
      #cards
      +getTopCard() : Card
      +isEmpty() : bool
      +shuffle()
    }
    class Card{
      #color
      #value
      +getColor() : str
      +getValue() : int
    }
    class Deck{
      +_init()
      +shuffle
    }
    class DiscardPile{
      #color
      +getColor() : str
    }
    class Hand{
      +getHand() : List[Card]
      +hasColor(string) : bool
    }
    class Expedition{
      #cards
      #color
      +addCard(Card)
      +removeCard(Card)
      +highestValue() : int
      +containsWager() : bool
      +getColor() : str
    }
```