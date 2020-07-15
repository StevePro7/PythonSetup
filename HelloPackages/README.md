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


PyCharm
open E:\GitHub\StevePro7\PythonSetup\HelloPackages\PyCharm\02-PackageExample

Terminal
(base) E:\GitHub\StevePro7\PythonSetup\HelloPackages\PyCharm\02-PackageExample>

pip install project/.
python -m unittest discover project


Use of the PYTHONPATH variable
https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file


How to correctly set PYTHONPATH for Visual Studio Code
will this work?
https://stackoverflow.com/questions/53653083/how-to-correctly-set-pythonpath-for-visual-studio-code


IMPORTANT


This VS Code sample works for unit tssts 
E:\GitHub\StevePro7\PythonSetup\HelloPackages\VScode\03-PackageExample

But the code runner Ctrl + Alt + N still failed
unless I change the following to global settings.json

"code-runner.runInTerminal": true,

and code runner works although we get the fluff
maybe if I set 
terminal.integrated.shell.windows

Reference:
https://stackoverflow.com/questions/50966876/vs-code-code-runner-doesnt-work-with-virtualenvs

Finally not sure if this is all because I don't have virtualenvs setup for project


IMPORTANT
when change settings.json file and .env file
ensure that we close VS Code and re-open
so that will be prompted to access PYTHONPATH 
going forward


VS Code on MAC
Could not create temporary directory: Permission denied
https://github.com/Microsoft/vscode/issues/63869



General
04-PackageExample
E:\GitHub\StevePro7\PythonSetup\HelloPackages

Launch PyCharm
open
E:\GitHub\StevePro7\PythonSetup\HelloPackages\04-PackageExample
from driver.src.module import getAge

Terminal
(base) E:\GitHub\StevePro7\PythonSetup\HelloPackages\04-PackageExample>
python -m  unittest discover driver


IMPORTANT
if in PyCharm the smart intellisense is annoying you then disable
File | Settings | Tools | Terminal
Smart command handling		UNCHECK
