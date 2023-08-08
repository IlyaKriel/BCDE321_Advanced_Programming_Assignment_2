from card import Card


class CardDeck:

    def __init__(self):
        self.doom_clock = 9
        self.card_deck = []
        self.deck_counter = 0

    def add_card_to_card_deck(self, image_number, event_9pm, event_10pm, event_11pm):
        card = Card(image_number, event_9pm, event_10pm, event_11pm)
        self.card_deck.append(card)
        self.deck_counter = len(self.card_deck)

    # need to draw a card (a random card)
    def get_card_event(self, target_event_time):
        return next((event for event in self.card_deck if event.get_event(target_event_time) == target_event_time))

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
