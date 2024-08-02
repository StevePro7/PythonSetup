Pytest
01-Aug-2024

Tutorials Point
https://www.tutorialspoint.com/pytest/index.htm


pip install pytest
pip install --upgrade pip
pytest -h


Files
test*
*test

pytest -v
verbosity

pytest test_square.py

SUBSTRING
pytest -k great


Grouping tests
@pytest.mark.<markername>
pytest -m <markername>

NB: the tutorial did not show this but found from previous example
MUST have the pytest.ini file
and define all the markers!!


Fixtures
functions run before each test function to which is applied
e.g. feed some data to the tests like DB conn, URL, input data

@pytest.fixture
pytest -k divisible -v


conftest.py
define fixture functions in [global] conftest.py file to make them
accessible across multiple test files


parameterizing tests
run the test against multiple ssets of inputs
@pytest.mark.parametrize


Xfail / Skip tests
pytest will execute the xfail test but will not be considered as part of
failed or passed tests
@pytest.mark.xfail

skip
pytest will skip teh test - will not be executed
@pytest.mark.skip


Stop test suite after N test failures
pytest --maxfail = <num>
pytest test_failure.py -v --maxfail 1
stopping after 1 failures


Pytest run tests in parallel
pip install pytest-xdist
pytest -n 3


Test Execution results in XML format
pytest test_multiplication.py -v --junitxml="result.xml"


SUMMARY
pytest -v
pytest <filename>
pytest -k <substring>
pytest -m <marker_name>
@pytest.fixture
conftest.py
@pytest.mark.parametrize
@pytest.mark.xfail
@pytest.mark.skip
pytest --maxfail = <num>
pytest -n <num>
pytest -v --junitxml="result.xml"