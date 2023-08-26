from card_deck import CardDeck
from ZIMP_game.models import player
from enviornment import Environment
from tile import Tile
from indoor_tile import IndoorTile
from indoor_tile_name import IndoorTileName
from outdoor_tile import OutdoorTile
from outdoor_tile_name import OutdoorTileName
from player import Player
import numpy as np



class Game:

    MAP_HEIGHT, MAP_WIDTH = (16, 16)
    # Using numpy package to create a 16 x 16 2D array of zeros
    game_map = np.zeros((MAP_HEIGHT, MAP_WIDTH), dtype=Tile)

    STARTING_Y, STARTING_X = (7, 7)
    current_tile = [STARTING_Y, STARTING_X]
    current_tile_object = game_map[current_tile[0], current_tile[1]]

    def __init__(self):
        self.environment = Environment()
        self.environment.shuffle_tiles()
        self.load_tile(IndoorTile(IndoorTileName.Foyer),
                       self.STARTING_Y, self.STARTING_X)
        self.player = Player()  # Create a Player object
        self.card_deck = CardDeck()  # Create a CardDeck object

    def load_tile(self, tile, y_cord, x_cord):
        """Loads tile onto game map."""
        self.game_map[y_cord, x_cord] = tile
        self.current_tile = [y_cord, x_cord]
        self.current_tile_object = self.game_map[y_cord, x_cord]

    def move(self, direction):
        """Move to a new direction"""

        # If moving out through the dining room to the patio
        if ((self.current_tile_object.name == IndoorTileName.Bathroom)
                & self.current_tile_object.white_arrows[direction]):
            self.place_patio(direction)

        # If in the Bathroom with no exits or all exits explored
        if ((self.current_tile_object.name == IndoorTileName.Bathroom)
                | self.is_all_exits_explored()):
            self.break_room()

        # If on a tile with no special features
        else:
            self.tile_direction_action(direction)

    def tile_direction_action(self, direction):
        """If there are no tiles in the next direction, draw a new tile;
        otherwise, revisit a tile"""
        tile_not_occupied = 0
        if self.generate_temp_location(direction) != tile_not_occupied:
            self.move_to_new_tile(direction)
        else:
            self.revisit_tile(direction)

    def move_to_new_tile(self, direction):
        """Executes when player moves to a direction with no occupied tile."""
        if self.can_exit(direction):
            self.draw_new_tile()
            self.match_exit_with_entry(direction)
            self.update_current_tile_position(direction)
            # How to check if valid?

    def can_exit(self, direction):
        """Returns True when valid exit direction is chosen
        for indoors/ outdoors tile"""
        if self.current_tile_object.exits[direction]:
            return True
        else:
            return False

    def update_current_tile_position(self, direction):
        """Updates current tile position based on exit direction"""
        match direction:
            case "north":
                self.current_tile = [self.current_tile[0] - 1, self.current_tile[1]]
            case "east":
                self.current_tile = [self.current_tile[0], self.current_tile[1] + 1]
            case "south":
                self.current_tile = [self.current_tile[0] + 1, self.current_tile[1]]
            case "west":
                self.current_tile = [self.current_tile[0], self.current_tile[1] - 1]
            case _:
                raise ValueError("Incorrect direction name!")
        # Add to game map
        self.game_map[self.current_tile[0],
                      self.current_tile[1]] = self.current_tile_object

    def revisit_tile(self, direction):
        """Revisits a tile"""
        match direction:
            case "north":
                self.current_tile = [self.current_tile[0] - 1, self.current_tile[1]]
            case "east":
                self.current_tile = [self.current_tile[0], self.current_tile[1] + 1]
            case "south":
                self.current_tile = [self.current_tile[0] + 1, self.current_tile[1]]
            case "west":
                self.current_tile = [self.current_tile[0], self.current_tile[1] - 1]
            case _:
                raise ValueError("Incorrect direction name!")

        self.current_tile_object = self.game_map[self.current_tile[0],
                                                 self.current_tile[1]]

    def is_all_exits_explored(self):
        """Returns true if all available exits are explored"""
        # ADJACENT_TILE = 1
        # Y_COORD = self.current_tile[0]
        # X_COORD = self.current_tile[1]
        empty_tile = 0
        all_exits_explored = False

        # if (self.game_map[Y_COORD + ADJACENT_TILE][X_COORD] != NO_TILES
        #     & self.game_map[Y_COORD - ADJACENT_TILE][X_COORD] != NO_TILES
        #     & self.game_map[Y_COORD][X_COORD + ADJACENT_TILE] != NO_TILES
        #     & self.game_map[Y_COORD][X_COORD - ADJACENT_TILE] != NO_TILES):
        #     all_exits_explored = True

        for direction, is_exit in self.current_tile_object.exits:
            if is_exit:
                if self.generate_temp_location(direction) == empty_tile:
                    return all_exits_explored
        all_exits_explored = True

        return all_exits_explored

    def break_room(self):
        """After the player battles the zombies and still have health left,
        the player chooses a new direction to exit"""
        NO_HEALTH = 0
        self.battle()
        if Player.health > NO_HEALTH:
            valid_direction = False
            direction = ""
            while not valid_direction:  # And not entry direction!
                direction = input("Please enter new direction.")
                valid_direction = self.check_direction(direction)
            self.game_map[self.current_tile[0],
                          self.current_tile[1]].exits[direction] = True
            self.move_to_new_tile(direction)

    @staticmethod
    def check_direction(direction):
        """Checks if the direction is a valid direction"""
        match direction:
            # Does not include entry direction!!
            case "north" | "east" | "south" | "west":
                return True
            case _:
                return False

    def place_patio(self, direction):
        """
        Moving from dining room to patio. Patio is now the new current tile.
        """
        self.current_tile_object = OutdoorTile(OutdoorTileName.Patio)
        self.match_patio(direction)
        self.update_current_tile_position(direction)

    def combat(self, num_zombies):
        """"For combating zombies"""
        if num_zombies > 0:
            # Get the player's attack score
            player_attack = self.player.attack

            # Calculate damage received based on player's attack and number of zombies
            damage_received = max(0, num_zombies - player_attack)
            damage_received = min(damage_received, 4)  # Max damage at 4

            # Update player's health and return combat result
            combat_result = player.take_damage(damage_received)
            return combat_result
        else:
            return "There are no zombies to combat."

    def find_totem(self):

    def bury_totem(self):


