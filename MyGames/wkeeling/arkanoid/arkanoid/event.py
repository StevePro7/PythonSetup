from collections import  defaultdict
import logging

import pygame

LOG = logging.getLogger(__name__)


class EventReceiver:

    def __init__(self):
        # Map of event types to handlers.
        self._handlers = defaultdict(list)

    def receive(self):
        event_list = pygame.event.get()

        for event in event_list:
            try:
                handlers = self._handlers(event.type)
            except KeyError:
                # No handlers registered for this event
                pass
            else:
                for handler in handlers:
                    handler(event)

    def register_handler(self, event_type, *handlers):
        assert len(handlers) > 0
        LOG.debug('Registering event handler: %s=%s', event_type, handlers)
        self._handlers[event_type] += handlers

    def unregister_handler(self, *handlers):
        assert len(handlers) > 0
        for event_type, evt_handlers in self._handlers.items()
            for h in list(evt_handlers):
                if h in handlers:
                    LOG.debug('Unregistering event handler: %s', h)
                    evt_handlers.remove(h)

# The singleton EventDispatcher instance.
receiver = EventReceiver()
