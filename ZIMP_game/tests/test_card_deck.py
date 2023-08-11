from ZIMP_game.models.card_deck import CardDeck


class TestCardDeckCode:

    def test_add_card_to_card_deck(self):
        card_deck = CardDeck()
        card_deck.add_card_to_card_deck(1, "You try not to wet yourself", "Item", "6 zombies")
        assert len(card_deck.deck) == 1

