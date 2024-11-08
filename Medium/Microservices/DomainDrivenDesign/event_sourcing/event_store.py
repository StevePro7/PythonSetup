from events.order_placed import OrderPlaced

# event_sourcing/event_store.py
class EventStore:
    def __init__(self):
        self.events = []

    def add_event(self, myevent):
        self.events.append(myevent)

    def get_events(self):
        return self.events

# Example usage
event_store = EventStore()
order_event = OrderPlaced(order_id=1, customer_name="John Doe", amount=150.0)
event_store.add_event(order_event)

# Replaying events
for event in event_store.get_events():
    print(event)