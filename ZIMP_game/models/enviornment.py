from indoor_tile_name import IndoorTileName
from outdoor_tile_name import OutdoorTileName
from indoor_tile import IndoorTile
from outdoor_tile import OutdoorTile
import random


class Environment:
    def __init__(self):
        self.is_indoors = True
        self.indoor_tiles = [IndoorTile(IndoorTileName.Bathroom),
                             IndoorTile(IndoorTileName.Kitchen),
                             IndoorTile(IndoorTileName.Storage),
                             IndoorTile(IndoorTileName.Evil_Temple),
                             IndoorTile(IndoorTileName.Family_Room),
                             IndoorTile(IndoorTileName.Dining_Room),
                             IndoorTile(IndoorTileName.Bedroom)]

        self.outdoor_tiles = [OutdoorTile(OutdoorTileName.Garden),
                              OutdoorTile(OutdoorTileName.Sitting_Area),
                              OutdoorTile(OutdoorTileName.Graveyard),
                              OutdoorTile(OutdoorTileName.Garage),
                              OutdoorTile(OutdoorTileName.Yard_One),
                              OutdoorTile(OutdoorTileName.Yard_Two),
                              OutdoorTile(OutdoorTileName.Yard_Three)]

    def shuffle_tiles(self):
        random.shuffle(self.indoor_tiles)
        random.shuffle(self.outdoor_tiles)

    def draw_new_tile(self):
        """Draw and store the new tile. Remove this new tile
        from the tile card pile"""
        FIRST_TILE_INDEX = 0
        if self.is_indoors:
            self.current_tile_object = self.indoor_tiles.pop(FIRST_TILE_INDEX)
            print("self.indoor_tiles")
        else:
            self.current_tile_object = self.outdoor_tiles.pop(FIRST_TILE_INDEX)

    def match_exit_with_entry(self, direction):
        """Perform actions so that old tile exit
        correspond with new tile entry"""
        check_exit_with_entry = True
        while check_exit_with_entry:
            match direction:
                case "north":
                    if self.current_tile_object.exits["south"]:
                        check_exit_with_entry = False
                    else:
                        self.rotate_tile()
                case "east":
                    if self.current_tile_object.exits["west"]:
                        check_exit_with_entry = False
                    else:
                        self.rotate_tile()
                case "south":
                    if self.current_tile_object.exits["north"]:
                        check_exit_with_entry = False
                    else:
                        self.rotate_tile()
                case "west":
                    if self.current_tile_object.exits["east"]:
                        check_exit_with_entry = False
                    else:
                        self.rotate_tile()
                case _:
                    raise ValueError("Not correct direction!")

    def rotate_tile(self):
        """Rotates new tile. Used for matching old tile exit
        to new tile entry"""
        temp_direction_array = [self.current_tile_object.exits["north"],
                                self.current_tile_object.exits["east"],
                                self.current_tile_object.exits["south"],
                                self.current_tile_object.exits["west"]]
        # First item becomes last item in the array
        # temp_value = temp_direction_array[0]
        # del temp_direction_array[0]
        # temp_direction_array.append(temp_value)
        temp_direction_array = temp_direction_array[1:] + \
                               [temp_direction_array[0]]
        # Reassigns new direction
        self.current_tile_object.exits["north"] = temp_direction_array[0]
        self.current_tile_object.exits["east"] = temp_direction_array[1]
        self.current_tile_object.exits["south"] = temp_direction_array[2]
        self.current_tile_object.exits["west"] = temp_direction_array[3]

        if (self.current_tile_object.name == IndoorTileName.Dining_Room
                or self.current_tile_object.name == OutdoorTileName.Patio):
            self.rotate_white_arrow()

    def match_patio(self, direction):
        """
        Rotates the patio so that its white arrow matches
        the white arrow of the dining room.
        """
        check_white_arrow = True
        while check_white_arrow:
            match direction:
                case "north":
                    if self.current_tile_object.white_arrows["south"]:
                        check_white_arrow = False
                    else:
                        self.rotate_tile()
                case "east":
                    if self.current_tile_object.white_arrows["west"]:
                        check_white_arrow = False
                    else:
                        self.rotate_tile()
                case "south":
                    if self.current_tile_object.white_arrows["north"]:
                        check_white_arrow = False
                    else:
                        self.rotate_tile()
                case "west":
                    if self.current_tile_object.white_arrows["east"]:
                        check_white_arrow = False
                    else:
                        self.rotate_tile()
                case _:
                    raise ValueError("Not correct direction!")

    def rotate_white_arrow(self):
        """Rotates new tile. Used for matching old tile exit
        to new tile entry"""
        temp_arrow_array = [self.current_tile_object.white_arrows["north"],
                            self.current_tile_object.white_arrows["east"],
                            self.current_tile_object.white_arrows["south"],
                            self.current_tile_object.white_arrows["west"]]
        # First item becomes last item in the array
        # temp_value = temp_direction_array[0]
        # del temp_direction_array[0]
        # temp_direction_array.append(temp_value)
        temp_arrow_array = temp_arrow_array[1:] + \
                           [temp_arrow_array[0]]
        # Reassigns new direction
        self.current_tile_object.white_arrows["north"] = temp_arrow_array[0]
        self.current_tile_object.white_arrows["east"] = temp_arrow_array[1]
        self.current_tile_object.white_arrows["south"] = temp_arrow_array[2]
        self.current_tile_object.white_arrows["west"] = temp_arrow_array[3]

    def generate_temp_location(self, direction):
        """Generate a temporary tile based on direction"""
        temp_location = ""
        match direction:
            case "north":
                temp_location = self.game_map[self.current_tile[0] - 1, self.current_tile[1]]
            case "east":
                temp_location = self.game_map[self.current_tile[0], self.current_tile[1] + 1]
            case "south":
                temp_location = self.game_map[self.current_tile[0] + 1, self.current_tile[1]]
            case "west":
                temp_location = self.game_map[self.current_tile[0], self.current_tile[1] - 1]
            case _:
                raise ValueError("Incorrect test direction name!")
        return temp_location
