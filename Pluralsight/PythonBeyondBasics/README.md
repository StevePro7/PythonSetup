README.md
06-Feb-2024

source
D:\BitBucket\SteveProXNA\actionstuff\Study\Plurasight\PythonBeyondBasics




format
https://www.datacamp.com/tutorial/f-string-formatting-in-python?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=157156373751&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=684592138751&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9067729&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na&gad_source=1&gclid=Cj0KCQiAzoeuBhDqARIsAMdH14HriWJvY2HCxZbFmcctDQZ0zBDdxZ6BmrbVpUgBXKmhpK1NRPTwD6caAjgqEALw_wcB


The whole shebang
which python3
#!/usr/bin/env python3


IMPORTANT
Chp11.
UnicodeError
does not have the following attributes
encoding
reason
object
start
end
BUT 
UnicodeDecodeError does and UnicodeError is base class of UnicodeDecodeError

Q. How do I know?
A. Debug ahd help(e) typed in the Debug console window


Python type hints
https://docs.python.org/3/library/typing.html


Python
methods beginning with underscore = private
Variables with a single underscore are considered "weakly private" in Python.
While no restrictions are enforced, it is a convention to indicate that these
Variables are intended for internal use within the class or module and should
not be accessed directly from outside i.e. violate encapsulation


Python naming conventions
https://www.techversantinfotech.com/python-naming-conventions-points-you-should-know

def public_method():
def _protected_method():
def __private_method();

packages	should be lowercase
methods 	should be lowercase
classes		should be Pascalcase	CapWord


Python methods: instance vs. class vs. static
https://realpython.com/instance-class-and-static-methods-demystified


Python ellipsis
https://medium.com/@mycodingmantras/demystifying-python-ellipsis-unleashing-the-power-of-the-three-dots-cad7fed70b4c

Python ellipsis (...) is a versatile object that 
- serves as a placeholder
- aids in array slicing
- enhances type hinting
- simplifies indexing multidimensional arrays
- indicates unfinished code parts