Mastering Testing in Python: A Theoretical Foundation (Part 1)
16-Oct-2024


https://blog.devgenius.io/mastering-testing-in-python-a-theoretical-foundation-part-1-d4457ac92587


Test doubles
mocks, stabs, fakes, dummies, spies


Mocks
objects that record interactions with your code during test
programmed to return specific values or simulated exceptions
used to verify behavior ensuring code interacts w/ dependencies as expected

e.g.
Ex04
mock verifies TransactionValidator class calls charge method
on the PaymentGateway dependency


Stubs
objects that provide predetermined responses to method calls
used to control behaviour of dependencies w/o executing actual logic
ideal for testing specific outcomes and scenarios

e.g.
Ex05
stub controls behavior of the InventoryManager dependency
return a predefined list of inventory items


Fakes
simplified implementation of real dependenies that are used in
place of the actual implementation
usually lighter and faster making tests more efficient
used to simulate successful or failed interactions w/ external dependencies

e.g.
Ex06
fake simulates the behavior of the SystemClock dependency
returning a predefined date and time


Dummies
objects that are passed around but never actually get used
typically used to fill parameter lists to satisfy method signatures

e.g.
Ex07
dummy fills the widget_loader parameter which is not actually
used in the test


Spies
objects that record info about interactions w/ your code similar
to mocks but focus on observing behavior rather than controlling it

e.g.
Ex08
spy used to observe the behavior of WeatherServicd class
verifying that it calls get_weather_data() method on WeatherAPI
dependency



