from zope.interface import Interface

class Animal(Interface):
   def eat(self, food) -> float:
       pass
   def sleep(self, hours) -> float:
       pass
