from card import Card
import random


class CardDeck:

    def __init__(self):
        self.doom_clock = 9
        self.card_deck = []
        self.deck_counter = 0
        self.discarded_cards = []

    def add_card_to_card_deck(self, image_number, event_9pm, event_10pm, event_11pm):
        card = Card(image_number, event_9pm, event_10pm, event_11pm)
        self.card_deck.append(card)
        self.deck_counter = len(self.card_deck)

    def return_card_if_not_discarded(self):
        # while the card is not in the discarded_cards return the card event
        # select a random card from the deck by using a random number for index selection.

        while True:
            random_number = random.randint(0, 8)
            random_card = self.card_deck[random_number]
            discarded_card = next((card for card in self.discarded_cards if card == random_card), None)

            if discarded_card != random_card:
                # add the card to the discarded_cards
                self.discarded_cards.append(random_card)
                # reduce the number of cards available to draw from
                self.reduce_deck_counter()
                return random_card

    # need to draw a card (a random card)
    def get_card_event(self):
        random_card = self.return_card_if_not_discarded()
        if random_card.get_event(self.doom_clock) == "Item":
            return self.get_card_item(False, random_card)
        else:
            return random_card.get_event(self.doom_clock)

    def get_card_item(self, draw_for_item, current_card=None):
        # get a card that hasn't been drawn/discarded
        # player chooses to draw a new card for an item
        if draw_for_item:
            random_card = self.return_card_if_not_discarded()
            return random_card.get_item()
        else:
            # player recieved an item from an event item being drawn
            return current_card.get_item()

    # reduce the deck_counter on player action
    def reduce_deck_counter(self):
        if self.deck_counter > 0:
            self.deck_counter -= 1
        else:
            # reset the deck_counter and increase the doom clock
            self.deck_counter = len(self.card_deck)
            # deck_counter = deck_size
            self.increase_doom_clock_counter_or_end()

    # check that the doom clock is not equal to 12 then increase the doom clock by 1
    def increase_doom_clock_counter_or_end(self):
        if self.doom_clock < 12:
            self.doom_clock += 1
        else:
            return f'The clock strikes {self.doom_clock}pm! You die!'

    # return the doom_clock as a string to display to the player
    def get_doom_clock(self):
        return f'{self.doom_clock}pm'
