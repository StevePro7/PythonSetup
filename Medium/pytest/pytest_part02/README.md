Mastering Testing in Python: Advanced Pytest Features and Best Practices (Part 2)
16-Oct-2024


https://blog.devgenius.io/mastering-testing-in-python-advanced-pytest-features-and-best-practices-part-2-10fa0d28e135


Pytest
assertions
== != < > in not


Ex01
pytest.raises
context manager checks if function raises specific exception


Run
pytest test_example.py      # Run a single test file
pytest tests/               # Run all tests in a directory
pytest -k test_example      # Run a specific test function
pytest -v test_example.py


Discovery
pytest --collect-only tests/


Advanced features

Ex02
Fixtures
manage test dependencies and setup / teardown processes
define reuasable objects or data that can be shared across tests
e.g.
pytest.fixture


Ex03
Fixture scopes
function    fixture destroyed at end of each test function
class       fixture destroyed during teardown of last test in class
module      fixture destroyed during teardown of last test in module
package     fixture destroyed during teardown of last test in package
session     fixture destroyed at end of test session


Ex04
Autouse fixtures
can be automatically used w/o being explicitly references


Ex05
Fixture factories
can be parameterized to produce multiple values


Ex06
Parameterizing fixtures
@pytest.mark.parametrize


Ex07
Fixture dependencies
fixtures can depend on other fixtures


Ex08
Teardown with yield


Ex09
Dynamic fixtures
adapt based on test requirements


Ex10
File I/O

Ex11
Configuration

Ex12
Test data
use fixtures to provide test data e.g. read from external file


Parameterization
Ex13
run the same test function multiple times w/ different input values








Sharing Fixtures Across Modules: Use conftest.py to define fixtures that can be shared across multiple test modules.

Ex14
pytest.param
add more metadata to each test case

NB:
multiple parametrize decorators
generates 4x test cases
(1,3), (1,4), (2,3), (2,4)

Ex15
Other options seem a bit overkill for now
Indirect Parametrization
Parametrizing Fixtures
External Data