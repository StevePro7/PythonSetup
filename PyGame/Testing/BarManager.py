from ServiceRegistry import ServiceRegistry
from FooManager import FooManager

class BarManager:

    def Initialize(self):
        print("BM steve Init")

    def LoadContent(self):
        print("BM steve Load #1")
        foo: FooManager = ServiceRegistry.get(FooManager.__name__)
        foo.LoadContent()

        print("BM steve Load #2")