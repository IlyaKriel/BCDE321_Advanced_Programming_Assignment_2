import sys

from ZIMP_game.models.card_deck import CardDeck
from ZIMP_game.models.player import Player


class Game:

    DISCARD_TWO_CARDS = 2

    def __init__(self):
        # self.environment = Environment()
        self.deck = CardDeck()
        self.player = Player()
        self.player_has_totem = False
        self.player_buried_totem = False

    # set up the indoor tile deck -> includes the evil temple
    # if on kitchen or garden tile end turn -> gain health +1
    # if no exit -> fight 3 zombies breaking through wall to create new exit of choice
    # set up the outdoor tile deck -> includes the graveyard

    # set up the player
    # set the player position -> current position

    # player_move_action -> because it combines player and environment
    # player_combat_action -> because it combines player and dev_card event
        # player action = fight or run away

    # set up the dev cards
    def setup_dev_card_and_item(self, image_number, item_name, uses, attack_modifier):
        deck = self.deck

        # add cards
        deck.add_card_to_card_deck(image_number)
        card = deck.find_card_that_matches_image_number(image_number)

        # set card item
        card.set_item(item_name, uses, attack_modifier)

    # set card event
    def setup_card_event(self, image_number, event_time, description, health_modifier=None):
        card = self.deck.find_card_that_matches_image_number(image_number)
        card.set_event(event_time, description, health_modifier)

    # game rule: discard two cards initially and each time the deck is shuffled
    def discard_two_cards(self):
        counter = Game.DISCARD_TWO_CARDS
        while counter > 0:
            self.deck.reduce_deck_counter()
            counter += counter - 1

    # player chooses to draw a dev_card to get an item
    def draw_dev_card_item(self, requirement):
        # check if the player is in the storage room or player drew item on previous card
        if requirement == CardDeck.ITEM_EVENT or requirement == "IndoorTileName.Storage":
            item = self.deck.get_card_item()
            self.player.add_item(item)
            item_card = next((card for card in self.deck.deck if card.item == item), None)
            item_image = item_card.get_item_image()
            item_image.show()

    # draw a dev_card when player moves to new tile
    def draw_dev_card_event(self):
        card = self.deck.get_card_if_not_discarded()
        card.get_item_image().show()
        return self.deck.get_card_event(card)

    def player_attempt_find_totem(self):
        # draw a dev_card to resolve
        self.draw_dev_card_event()
        # if the player has health then
        if self.player.health != 0:
            self.player_has_totem = True

    def player_attempt_bury_totem(self):
        # draw a dev_card to resolve
        self.draw_dev_card_event()
        # if the player has health then
        if self.player.health != 0:
            self.player_buried_totem = True
            self.win_condition_result()

    # check win condition
    def win_condition_result(self):
        if self.player_has_totem and self.player_buried_totem:
            sys.exit("You've WON!")
