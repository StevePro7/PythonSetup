Instructions
13/07/2020


Launch PyCharm
Create New Project
E:\GitHub\StevePro7\PythonSetup\HelloPackages\01-PackageExample
Create


right click 01-PackageExample
New | Python package
example_pkg

right click example_pkg
New | Python package
tests
add all code as before

Start | run | cmd
cd E:\GitHub\StevePro7\PythonSetup\HelloPackages
cd 01-PackageExample
python

print(a)
a = stackoverflow.hello()
from example_pkg import stackoverflow
a = stackoverflow.hello()
print(a)

print(a)
a = sf.hello()
from example_pkg import stackoverflow as sf
a = sf.hello()
print(a)


MAC + Linux
cd
cd Github/StevePro7/PythonSetup/HelloPackages
cd 01-PackageExample

print(a)
a = stackoverflow.hello()
from example_pkg import stackoverflow
a = stackoverflow.hello()
print(a)

print(a)
a = sf.hello()
from example_pkg import stackoverflow as sf
a = sf.hello()
print(a)


FINALLY
terminal
cd 01-PackageExample

pip install example_pkg/.
python -m unittest discover example_pkg