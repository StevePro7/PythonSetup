import unittest

import arkanoid.event as event


class TestEventReceiver(unittest.TestCase):

    def test_register_handler(self):
        def handler():
            pass

        event.receiver.register_handler('foo', handler)

        self.assertIn(handler, event.receiver._handlers['foo'])

    def test_register_multiple_handlers(self):
        def handler1():
            pass

        def handler2():
            pass

        event.receiver.register_handler('foo', handler1, handler2)

        self.assertIn(handler1, event.receiver._handlers['foo'])
        self.assertIn(handler2, event.receiver._handlers['foo'])

    def test_register_handler_raises_exception_when_no_handler(self):
        with self.assertRaises(AssertionError):
            event.receiver.register_handler('foo')

    def test_unregister_handler(self):
        def handler():
            pass

        event.receiver._handlers['test_event'].append(handler)

        event.receiver.unregister_handler(handler)

        self.assertNotIn(handler, event.receiver._handlers['test_event'])

    def test_unregister_multiple_handlers(self):
        def handler1():
            pass

        def handler2():
            pass

        event.receiver._handlers['test_event'] += handler1, handler2

        event.receiver.unregister_handler(handler1, handler2)

        self.assertNotIn(handler1, event.receiver._handlers['test_event'])
        self.assertNotIn(handler2, event.receiver._handlers['test_event'])

    def test_unregister_handler_raises_exception_when_no_handler(self):
        with self.assertRaises(AssertionError):
            event.receiver.unregister_handler()




