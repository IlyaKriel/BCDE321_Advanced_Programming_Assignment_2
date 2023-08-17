class Player:

    # constructor
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
        # empty list to store players items
        self.inventory = []

    # adds item to inventory if inventory has less than 2 items
    def add_item(self, item):
        if len(self.inventory) < 2:
            self.inventory.append(item)
            print(f"You've acquired {item.name}.")

    # item gets removed if item is in inventory
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def use_item(self, item, target=None):
        if item in self.inventory:
            if item.name == "Oil":
                print("You've thrown oil to avoid damage while running away.")
                self.remove_item(item)
            elif item.name == "Gasoline":
                print("You've used gasoline to clear zombies on your tile.")
                self.remove_item(item)
            elif item.name in ["Board w/ Nails", "Grisly femur", "Golf club", "Chainsaw", "Machete"]:
                if target == "zombies":
                    damage = max(0, target - self.attack)
                    print(f"You've used {item.name} to attack zombies. You dealt {damage} damage.")
                else:
                    print(f"{item.name} can only be used in combat.")
            elif item.name == "Can of soda":
                print("You've consumed a can of soda to regain 2 health points.")
                self.health = min(6, self.health + 2)
                self.remove_item(item)
            elif item.name == "Candle":
                print("You've used a candle to clear zombies on your tile.")
                self.remove_item(item)
            else:
                print("Invalid item.")
        else:
            print("You don't have that item.")

    def run_away(self):
        print("You've run away from the zombies, losing 1 health point.")
        self.health = max(0, self.health - 1)

    def cower(self):
        print("You've decided to cower and hide. You regain 3 health points.")
        self.health = min(6, self.health + 3)

    def take_damage(self, damage):
        print(f"You've taken {damage} damage.")
        self.health = max(0, self.health - damage)

    def combat(self, num_zombies):
        damage_received = max(0, num_zombies - self.attack)
        damage_received = min(damage_received, 4)  # Max damage at 4
        self.take_damage(damage_received)
        print(f"You're in combat with {num_zombies} zombies.")
        print(f"You've taken {damage_received} damage.")


