from ZIMP_game.models.card import Card
from random import randrange


class CardDeck:

    DOOM_CLOCK_START_TIME = 9
    GET_ITEM_EVENT = "Item"

    def __init__(self):
        self.doom_clock = CardDeck.DOOM_CLOCK_START_TIME
        self.deck = []
        self.deck_counter = len(self.deck)
        self.discarded_cards = []
        self.item_event = CardDeck.GET_ITEM_EVENT

    def add_card_to_card_deck(self, image_number):
        card = Card(image_number)
        self.deck.append(card)
        self.deck_counter = len(self.deck)

    def add_card_to_discarded_cards(self):
        while True:
            random_number = randrange(len(self.deck))
            random_card = self.deck[random_number]
            discarded_card = next((card for card in self.discarded_cards if card == random_card), None)

            if discarded_card != random_card:
                self.discarded_cards.append(random_card)
                self.reduce_deck_counter()
                break

    def get_card_if_not_discarded(self):
        # while the card is not in the discarded_cards return the card
        # select a random card from the deck by using a random number for index selection

        while True:
            random_number = randrange(len(self.deck))
            random_card = self.deck[random_number]
            discarded_card = next((card for card in self.discarded_cards if card == random_card), None)

            if discarded_card != random_card:
                # add the card to the discarded_cards
                self.discarded_cards.append(random_card)
                # reduce the number of cards available to draw from
                self.reduce_deck_counter()
                return random_card

    def get_card_event(self):
        random_card = self.get_card_if_not_discarded()
        if random_card.get_event(self.doom_clock) == self.item_event:
            return "Optional: draw new card for item"
        else:
            return random_card.get_event(self.doom_clock)

    def get_card_item(self):
        # get a card that hasn't been drawn/discarded
        # player chooses to draw a new card for an item
        random_card = self.get_card_if_not_discarded()
        return random_card.get_item()

    # reduce the deck_counter on player action
    def reduce_deck_counter(self):
        if self.deck_counter > 0:
            self.deck_counter -= 1
        else:
            # reset the deck_counter and increase the doom clock
            self.deck_counter = len(self.deck)
            # deck_counter = deck_size
            self.increase_doom_clock_counter_or_end()

    # check that the doom clock is not equal to 12 then increase the doom clock by 1
    def increase_doom_clock_counter_or_end(self):
        if self.doom_clock < 12:
            self.doom_clock += 1
            self.discarded_cards.clear()
        else:
            return f'The clock strikes {self.doom_clock}pm! You die!'

    # return the doom_clock as a string to display to the player
    def get_doom_clock(self):
        return f'{self.doom_clock}pm'
