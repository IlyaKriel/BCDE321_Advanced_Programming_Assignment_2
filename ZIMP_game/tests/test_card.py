from ZIMP_game.models.card import Card


class TestCardCode:

    def test_set_item(self):
        card = Card("1")
        card.set_item("Chainsaw", 2, 3)
        assert card.item is not None

    def test_get_item(self):
        card = Card("1")
        card.set_item("Chainsaw", 2, 3)
        item = card.get_item()
        assert item.item_name == "Chainsaw"
        assert item.uses == 2
        assert item.attack_modifier == 3

    def test_get_event(self):
        card = Card("1")
        card.set_event(9, "You try hard not to wet yourself")
        card.set_event(10, "Item")
        card.set_event(11, "Zombies", 6)
        event = card.get_event(11)
        assert event.description == "Zombies"
        assert event.health_modifier == 6

    def test_get_item_image(self):
        card = Card("1")
        image = card.get_item_image()
        assert image is not None
