class Player:

    INITIAL_PLAYER_HEALTH = 6
    INITIAL_PLAYER_ATTACK = 1

    # constructor
    def __init__(self):
        self.attack = Player.INITIAL_PLAYER_ATTACK
        self.health = Player.INITIAL_PLAYER_HEALTH
        # empty list to store players items
        self.inventory = []
        self.found_totem = False
        self.buried_totem = False

    # adds item to inventory if inventory has less than 2 items
    def add_item(self, item):
        if len(self.inventory) < 2:
            self.inventory.append(item)
            return f"You've acquired {item.get_item_name()}."

    # item gets removed if item is in inventory
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

# need to fix this
    def use_item(self, item, target=None, num_zombies=None):
        if item in self.inventory:
            if target == "self":
                return "You don't have that item."

            if item.get_item_name() == "Oil":
                self.remove_item(item)
                return "You've thrown oil to avoid damage while running away."
            elif item.get_item_name() == "Gasoline":
                self.remove_item(item)
                return "You've used gasoline to clear zombies on your tile."
            elif item.get_item_name() == "Candle":
                self.remove_item(item)
                oil_item = next((inv_item for inv_item in self.inventory if inv_item.get_item_name() == "Oil"), None)
                gasoline_item = next(
                    (inv_item for inv_item in self.inventory if inv_item.get_item_name() == "Gasoline"), None)

                if oil_item or gasoline_item:
                    if oil_item and oil_item.get_item_uses() > 0:
                        self.remove_item(oil_item)
                        return ("You've used a candle combined with oil to kill all zombies on your tile without "
                                "taking damage.")
                    elif gasoline_item and gasoline_item.get_item_uses() > 0:
                        self.remove_item(gasoline_item)
                        return ("You've used a candle combined with gasoline to kill all zombies on your tile without "
                                "taking damage.")
                    else:
                        return "You've already used up all available uses of oil and gasoline."
                else:
                    return "You need either oil or gasoline to combine with the candle."

            elif item.get_item_name() == "Chainsaw":
                gasoline_item = next(
                    (inv_item for inv_item in self.inventory if inv_item.get_item_name() == "Gasoline"), None)
                chainsaw_item = next(
                    (inv_item for inv_item in self.inventory if inv_item.get_item_name() == "Chainsaw"), None)

                if gasoline_item and gasoline_item.get_item_uses() > 0:
                    self.remove_item(gasoline_item)
                    if chainsaw_item:
                        chainsaw_item.increment_item_uses(2)
                        self.remove_item(chainsaw_item)
                        return "You've combined gasoline with the chainsaw to give it two more uses."
                    else:
                        return "You don't have the chainsaw to combine with gasoline."
                else:
                    return "You need gasoline to combine with the chainsaw."

            elif item.get_item_name() in ["Board w/ Nails", "Grisly femur", "Golf club", "Chainsaw", "Machete"]:
                if target == "zombies":
                    damage = max(0, num_zombies - (self.attack + item.get_item_attack_modifier()))
                    self.remove_item(item)
                    return f"You've used {item.get_item_name()} to attack zombies. You dealt {damage} damage."
                else:
                    self.remove_item(item)
                    return f"{item.get_item_name()} can only be used in combat."

            elif item.get_item_name() == "Can of soda":
                self.health = min(6, self.health + 2)
                self.remove_item(item)
                return "You've consumed a can of soda to regain 2 health points."

            else:
                self.remove_item(item)
                return "You don't have that item."
        else:
            return "You don't have that item."

    def run_away(self):
        self.health = max(0, self.health - 1)
        return "You've run away from the zombies, losing 1 health point."

    def cower(self):
        self.health = min(6, self.health + 3)
        return "You've decided to cower and hide. You regain 3 health points."

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        return f"You've taken {damage} damage."

    def combat(self, num_zombies):
        damage_received = max(0, num_zombies - self.attack)
        damage_received = min(damage_received, 4)  # Max damage at 4
        self.take_damage(damage_received)
        return f"You're in combat with {num_zombies} zombies.\nYou've taken {damage_received} damage."


