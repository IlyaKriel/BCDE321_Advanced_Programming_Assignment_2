from PIL import Image
from models.item import Item


class Card:
    
    def __init__(self, image_number, event_9pm, event_10pm, event_11pm):
        self.event_9pm = event_9pm
        self.event_10pm = event_10pm
        self.event_11pm = event_11pm
        self.image = Image.open(f'../images/card_{image_number}.JPG')
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
        return self.image.show()
