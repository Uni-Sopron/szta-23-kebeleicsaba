# Game
## init variables
- players
- table
- decks
## use cases
- create players, deck
- game flow 

# Player
## init variables
- name
- points
- hand_cards
## use cases
- get name, points, hand_cards
- set name, points
- add card
- play_card_to_expeditions

# Card
## init variables
- value
- color
- type
## use cases
- get value, color, type

# Deck
## init variables
- cards
## use cases
- shuffle
- get_a_card

# Table
## init variables
- expeditions (keys = colors, values = cards)
## use cases
- add_card_to_expedition
- calculate_expedition_points
- get_expeditions