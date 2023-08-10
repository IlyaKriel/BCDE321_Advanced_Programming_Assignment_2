class Item:

    def __init__(self, item_name, uses, attack_modifier):
        self.item_name = item_name
        self.uses = uses
        self.attack_modifier = attack_modifier

    def get_item_name(self):
        return self.item_name

    def get_item_uses(self):
        return self.uses

    def get_item_attack_modifier(self):
        return self.attack_modifier

    def increase_item_uses(self):
        self.uses += 1

    def decrease_item_uses(self):
        self.uses -= 1
