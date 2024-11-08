# events/event_dispatcher.py
class EventDispatcher:
    def __init__(self):
        self.handlers = []

    def register_handler(self, handler):
        self.handlers.append(handler)

    def dispatch(self, event):
        for handler in self.handlers:
            handler(event)

# Example handler function
def order_placed_handler(event):
    print(f"Handling event: {event}")

# Registering and dispatching an event
dispatcher = EventDispatcher()
dispatcher.register_handler(order_placed_handler)

# Usage
from events.order_placed import OrderPlaced

order_event = OrderPlaced(order_id=1, customer_name="John Doe", amount=150.0)
dispatcher.dispatch(order_event)