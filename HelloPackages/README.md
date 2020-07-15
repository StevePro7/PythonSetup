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


14/07/2020
from MyPackage.MyFoo import MyBar
works

but this doesn't
from MyFoo import MyBar

PyCharm terminal
cd E:\GitHub\StevePro7\PythonSetup\HelloPackages\PyCharm\01-PackageExample
pip install MyPackage/.

python -m unittest discover MyPackage
python -m unittest discover example_pkg


Launch VS Code
Open folder
D:\Azure\Galileo-driver
pip install driver/.
python -m unittest discover driver


15/07/2020
E:\GitHub\StevePro7\PythonSetup\HelloPackages\VScode\02-PackageExample

follow example here to get src + teste in VS Code
https://binx.io/blog/2020/03/05/setting-python-source-folders-vscode