```mermaid
classDiagram
    Game --o "2" Player
    Game --o "1" Deck
    Game --o "5" DiscardPile
    Player --o "1" Hand
    Player --o "5" Expedition
    Expedition *-- "*" Card
    AbstractPile *-- "*" Card
    AbstractPile <|-- Deck
    AbstractPile <|-- DiscardPile
    class Game{
      #players
      #deck
      #discardPiles
      #currentPlayer
      #currentTurn
      +start()
      +end() : dict
      +turn(Player, dict)
      +isGameOver() : bool
    }
    class Player{
      #name
      #hand
      #expeditions
      #points
      +playCard(Card)
      +discardCard(Card, DiscardPile)
      +drawCard(AbstractPile)
      +calcPoints()
      +getPoints()
    }
    class AbstractPile{
      #cards
      +drawCard() : Card
      +isEmpty() : bool
    }
    class Card{
      #color
      #value
      +getColor() : str
      +getValue() : int
    }
    class Deck{
      +_init()
      +shuffle()
    }
    class DiscardPile{
      #color
      +getColor() : str
      +addCard(Card)
      +displayTopCard()
    }
    class Hand{
      #cards
      +getHand() : List[Card]
      +hasColor(string) : bool
      +removeCard(Card)
      +addCard(Card)
    }
    class Expedition{
      #cards
      #color
      +addCard(Card)
      +getAllCards() : list[Card]
      +highestValue() : int
      +getColor() : str
      +getPoints() : int
    }
```