from PIL import Image

from ZIMP_game.models.event import Event
from ZIMP_game.models.item import Item


class Card:

    FILE_LOCATION = "../images/card_"
    FILE_EXTENSION = ".JPG"

    def __init__(self, image_number):
        self.event_9pm = None
        self.event_10pm = None
        self.event_11pm = None
        self.image = Image.open("%s%s%s" % (Card.FILE_LOCATION, image_number, Card.FILE_EXTENSION))
        self.item = None

    def set_event(self, event_time, description, health_modifier=None):
        event = Event(description, health_modifier)
        match event_time:
            case 9:
                self.event_9pm = event
            case 10:
                self.event_10pm = event
            case 11:
                self.event_11pm = event
        pass

    def set_item(self, item_name, uses, attack_modifier):
        self.item = Item(item_name, uses, attack_modifier)
    
    def get_event(self, event_time):
        match event_time:
            case 9:
                return self.event_9pm
            case 10:
                return self.event_10pm
            case 11:
                return self.event_11pm
    
    def get_item(self):
        return self.item

    def get_item_image(self):
        return self.image
