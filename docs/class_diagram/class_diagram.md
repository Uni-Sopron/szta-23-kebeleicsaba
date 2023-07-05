```mermaid
classDiagram
    Game --> "*" Player : has
    Game --> "1" Deck : has
    Game --> "5" DiscardPile : has
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
      #currentPlayer
      +start()
      +end()
      +calculateScores()
      +turn(Player, dict)
    }
    class Player{
      #name
      #hand
      #expeditions
      +playCard(Card, str)
      +discardCard(Card, DiscardPile)
      +drawCard(AbstractPile)
      +selectCard(Card) : Card
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
      #cards
      +getHand() : List[Card]
      +hasColor(string) : bool
      +removeCard(Card)
    }
    class Expedition{
      #cards
      #color
      +addCard(Card)
      +highestValue() : int
      +getColor() : str
    }
```