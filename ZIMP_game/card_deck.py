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

    # need to draw a card (a random card)
    def get_card_event(self):
        # while the card is not in the discarded_cards return the card event == doom_counter
        # select a random card from the deck
        # get a random number 0-8

        while True:
            random_number = random.randint(0, 8)
            random_card = self.card_deck[random_number]
            discarded_card = next((card for card in self.discarded_cards if card == random_card), None)

            if discarded_card != random_card:
                # add the card to the discarded_cards
                self.discarded_cards.append(random_card)
                # reduce the number of cards available to draw from
                self.reduce_deck_counter()
                return random_card.get_event(self.doom_clock)

    def get_card_item(self, discard_card):
        # if discard a card to get an item -> add card to the discarded_cards & reduce_deck_counter
        if discard_card:

        # else get random card not in discarded_cards to return the card item
        # & then add card to the discarded_cards & reduce_deck_counter
        pass

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
