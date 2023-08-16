class Event:

    def __init__(self, description, health_modifier=None):
        self.description = description
        self.health_modifier = health_modifier

    def get_event_description(self):
        return self.description

    def get_event_health_modifier(self):
        return self.health_modifier
