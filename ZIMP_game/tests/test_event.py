from ZIMP_game.models.event import Event


class TestEventCode:

    def test_get_event_description(self):
        event = Event("Zombies", 6)
        assert event.get_event_description() == "Zombies"

    def test_get_event_health_modifier(self):
        event = Event("Zombies", 6)
        assert event.get_event_health_modifier() == 6
