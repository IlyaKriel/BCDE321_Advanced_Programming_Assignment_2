import numpy as np
import random

from ZIMP_game.models.indoor_tile_names import IndoorTileNames
from ZIMP_game.models.tile import Tile


class Environment:

    MAP_HEIGHT, MAP_WIDTH = (16, 16)
    STARTING_ROW, STARTING_COLUMN = (7, 7)

    def __init__(self):
        self.indoor_tile_names = [member.value for member in IndoorTileNames]
        self.outdoor_tile_names = [member.value for member in IndoorTileNames]
        self.indoor_tile_deck = []
        self.outdoor_tile_deck = []
        self.visited_tiles = []
        self.current_position = None
        self.current_tile = None
        self.previous_tile = None
        # Using numpy package to create a 16 x 16 2D array of zeros
        self.game_map = np.zeros((Environment.MAP_HEIGHT, Environment.MAP_WIDTH), dtype=Tile)
        self.indoor = True

    def set_up_both_tile_decks(self, tile_name, tile_image_number, north_bool, east_bool, south_bool, west_bool):
        tile = Tile(tile_name, tile_image_number)
        tile.set_tile_doorways(north_bool, east_bool, south_bool, west_bool)
        if tile_name in self.indoor_tile_names:
            self.indoor_tile_deck.append(tile)
        elif tile_name in self.outdoor_tile_names:
            self.indoor_tile_deck.append(tile)
        else:
            return "That tile doesn't exist."

    def set_and_move_to_tile(self, tile, row, column):
        # initial tile placement
        if tile.get_tile_name() == IndoorTileNames.FOYER.value:
            self.game_map[Environment.STARTING_ROW, Environment.STARTING_COLUMN] = tile
            self.current_position = [Environment.STARTING_ROW, Environment.STARTING_COLUMN]
            self.previous_tile = self.current_tile
            self.current_tile = tile
            self.visited_tiles.append(tile)

        # check if the map position is valid to place tile
        if self.game_map[row, column] == 0:
            # check if the tile doesn't cut off another tile's entrance
            # check if the tile's entrance isn't being blocked by another tile
            # if either condition is true and rotate doesn't solve the check -> redraw a new tile
            self.game_map[row, column] = tile
            self.previous_tile = self.current_tile
            self.current_position = [row, column]
            self.current_tile = self.game_map[row, column]
            self.visited_tiles.append(tile)

            # if tile.get_tile_name() == IndoorTileNames.DINING_ROOM.value:

            # if evil_temple hasn't been drawn

            # check if the player transition from indoor to outdoor or vice versa?
            # get the exit key
            # loop through different grid direction modifiers
            # if exit key == "North" and
            # draw a random tile from indoor_deck if indoor == True

    def draw_tile(self):
        # first draw must be foyer
        if self.game_map[Environment.STARTING_ROW, Environment.STARTING_COLUMN] == 0:
            initial_tile = next((tile for tile in self.indoor_tile_deck
                                 if tile.get_tile_name() == IndoorTileNames.FOYER.value), None)
            return initial_tile

        if self.indoor:
            while True:
                random_number = random.randrange(len(self.indoor_tile_deck))
                random_tile = self.indoor_tile_deck[random_number]
                # check that the tile hasn't been visited
                visited_tile = next((tile for tile in self.indoor_tile_deck if tile in self.visited_tiles), None)

                if random_tile != visited_tile:
                    return random_tile
        else:
            while True:
                random_number = random.randrange(len(self.outdoor_tile_deck))
                random_tile = self.outdoor_tile_deck[random_number]
                # check that the tile hasn't been visited
                visited_tile = next((tile for tile in self.indoor_tile_deck if tile in self.visited_tiles), None)

                if random_tile != visited_tile:
                    return random_tile

