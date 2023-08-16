from ZIMP_game.models.card_deck import CardDeck


class TestCardDeckCode:

    def test_add_card_to_card_deck(self):
        card_deck = CardDeck()
        card_deck.add_card_to_card_deck(1, "You try not to wet yourself", "Item", "6 zombies")
        assert len(card_deck.deck) == 1

    def test_add_card_to_discarded_cards(self):
        card_deck = CardDeck()
        card_deck.add_card_to_card_deck(1, "You try not to wet yourself", "Item", "6 zombies")
        card_deck.add_card_to_discarded_cards()
        assert len(card_deck.discarded_cards) == 1

    def test_get_card_if_not_discarded(self):
        card_deck = CardDeck()
        card_deck.add_card_to_card_deck(1, "You try not to wet yourself", "Item", "6 zombies")
        card_deck.add_card_to_card_deck(2, "4 zombies", "You sense your impending doom - 1 health", "Item")
        card_deck.add_card_to_card_deck(3, "You try not to wet yourself", "Item", "6 zombies")
        card_deck.add_card_to_discarded_cards()
        card = card_deck.get_card_if_not_discarded()
        assert card != card_deck.discarded_cards[0]

    def test_get_card_event(self):
        card_deck = CardDeck()
        card_deck.add_card_to_card_deck(1, "You try not to wet yourself", "Item", "6 zombies")
        card_event = card_deck.get_card_event()
        assert card_event == "You try not to wet yourself"

    def test_get_card_item(self):
        card_deck = CardDeck()
        card_deck.add_card_to_card_deck(1, "You try not to wet yourself", "Item", "6 zombies")
        card = card_deck.deck[0]
        card.set_item("Chainsaw", 2, 3)
        item = card_deck.get_card_item()
        assert item is not None

    def test_reduce_deck_counter(self):
        card_deck = CardDeck()
        card_deck.add_card_to_card_deck(1, "You try not to wet yourself", "Item", "6 zombies")
        card_deck.add_card_to_card_deck(2, "4 zombies", "You sense your impending doom - 1 health", "Item")
        card_deck.add_card_to_card_deck(3, "You try not to wet yourself", "Item", "6 zombies")
        card_deck.reduce_deck_counter()
        assert card_deck.deck_counter == 2

    def test_increase_doom_clock_counter_or_end(self):
        card_deck = CardDeck()
        card_deck.increase_doom_clock_counter_or_end()
        assert card_deck.doom_clock == 10

    def test_get_doom_clock(self):
        card_deck = CardDeck()
        assert card_deck.get_doom_clock() == "9pm"
