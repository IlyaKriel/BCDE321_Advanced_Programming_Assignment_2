from PIL import Image
from ZIMP_game.models.item import Item


class Card:

    FILE_LOCATION = "../images/card_"
    FILE_EXTENSION = ".JPG"

    def __init__(self, image_number, event_9pm, event_10pm, event_11pm):
        self.event_9pm = event_9pm
        self.event_10pm = event_10pm
        self.event_11pm = event_11pm
        self.image = Image.open("%s%s%s" % (Card.FILE_LOCATION, image_number, Card.FILE_EXTENSION))
        self.item = None
        
    def set_item(self, item_name, uses, attack_modifier):
        self.item = Item(item_name, uses, attack_modifier)
    
    def get_event(self, event_time):
        match event_time:
            case 9:
                return self.event_9pm
            case 10:
                return self.event_10pm
            case 11:
                return self.event_10pm
    
    def get_item(self):
        return self.item

    def get_item_image(self):
        return self.image
