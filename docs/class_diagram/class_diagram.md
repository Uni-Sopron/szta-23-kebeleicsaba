```mermaid
classDiagram
    Game --> "*" Player : has
    Game --> "1" Deck : has
    Game --> "1" DiscardPile : has
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
      #discardPile
      #expeditions
      #currentPlayer
      +start()
      +end()
      +calculateScores()
      +turn(Player)
    }
    class Player{
      #name
      #points
      +playCard(Card, Expedition)
      +discardCard(Card)
      +drawCard(AbstractPile)
      +selectCard() : Card
    }
    class AbstractPile{
      #cards
      +addCard(Card)
      +removeCard(Card)
    }
    class Card{
      #color
      #value
    }
    class Deck{
      +shuffle()
      +isEmpty() : bool
      +topCard() : Card
    }
    class DiscardPile{
      #color
      +topCard() : Card
    }
    class Hand{
      +displayHand()
      +hasColor(string) : bool
    }
    class Expedition{
      #color
      +addCard(Card)
      +highestValue() : int
      +containsWager() : bool
    }

```