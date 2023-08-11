from ZIMP_game.models.item import Item


class TestItemCode:

    # basic tests for the Item class
    def test_get_item_name(self):
        item = Item("chainsaw", 2, 3)
        item_name = item.get_item_name()
        assert item_name == "chainsaw"

    def test_get_item_uses(self):
        item = Item("chainsaw", 2, 3)
        item_uses = item.get_item_uses()
        assert item_uses == 2

    def test_get_item_attack_modifier(self):
        item = Item("chainsaw", 2, 3)
        item_attack_modifier = item.get_item_attack_modifier()
        assert item_attack_modifier == 3

    def test_increase_item_uses(self):
        item = Item("chainsaw", 2, 3)
        item.increase_item_uses()
        assert item.get_item_uses() == 3

    def test_decrease_item_uses(self):
        item = Item("chainsaw", 2, 3)
        item.decrease_item_uses()
        assert item.get_item_uses() == 1
