from models.card import Card


class TestCardCode:

    def test_set_item(self):
        card = Card("1", "a", "b", "c")
        card.set_item("Chainsaw", 2, 3)
        assert card.item is not None

    def test_get_item(self):
        card = Card("1", "a", "b", "c")
        card.set_item("Chainsaw", 2, 3)
        item = card.get_item()
        assert item.item_name == "Chainsaw"
        assert item.uses == 2
        assert item.attack_modifier == 3

    def test_get_event(self):
        card = Card("1", "Don't pee yourself", "Item", "6 zombies")
        card.set_item("Chainsaw", 2, 3)
        event = card.get_event(9)
        assert event == "Don't pee yourself"

    def test_get_item_image(self):
        card = Card("1", "Don't pee yourself", "Item", "6 zombies")
        card.set_item("Chainsaw", 2, 3)
