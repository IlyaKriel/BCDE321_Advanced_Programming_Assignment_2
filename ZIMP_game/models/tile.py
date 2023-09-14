from collections import deque
from PIL import Image


class Tile:

    TILE_SIDES = ["North", "East", "South", "West"]
    FILE_LOCATION = "../images/tile_"
    FILE_EXTENSION = ".JPG"
    SPECIAL_EXIT_ROOMS = ["dining_room", "patio"]

    def __init__(self, tile_name, tile_image_number):
        self.name = tile_name
        self.doorways = {}
        self.tile_sides = Tile.TILE_SIDES
        self.image = Image.open("%s%s%s" % (Tile.FILE_LOCATION, tile_image_number, Tile.FILE_EXTENSION))
        self.exit = {}

    def get_tile_name(self):
        return self.name

    def set_tile_doorways(self, north_boolean, east_boolean, south_boolean, west_boolean):
        temp_list = [north_boolean, east_boolean, south_boolean, west_boolean]
        for side in self.tile_sides:
            list_index = 0
            if side in self.doorways.keys():
                side_value = temp_list[list_index]
                self.doorways[side] = side_value
                list_index += list_index + 1
        if self.name in Tile.SPECIAL_EXIT_ROOMS:
            self.exit[self.tile_sides[0]] = True

    def get_tile_doorways(self):
        return self.tile_sides

    def rotate_tile(self):
        deque_object = deque(self.doorways)
        deque_object.rotate(1)
        doorways_list = list(deque_object)
        exit_key = list(self.exit.keys())[0]
        self.exit[exit_key] = doorways_list[0]
        self.doorways = {e[0]: e[1] for e in doorways_list}

    # method returns a key value pair or False
    def get_tile_exit(self):
        return self.exit
