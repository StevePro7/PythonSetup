README.md
21-Jul-2024

pip install pybind11
pip install --upgrade pip


touch example.cpp
python setup.py build_ext --inplace

# First time??
pip install example

NB: I tried to update setup.py and change the version
but it did not seem to capture??
Maybe can only be done once