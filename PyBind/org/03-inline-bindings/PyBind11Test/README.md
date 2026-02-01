PyBind11Test
06-Dec-2025

cd ~/GitHub/StevePro9/PythonSetup/PyBind  
mkdir -p PyBind11Test  
uv init --python 3.11.11  

Launch PyCharm  
Open project  
~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test    

Creates .venv  
Otherise  
source .venv/bin/activate  

uv add pybind11
#uv pip install pybind11  
uv sync  

which python  
~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test/.venv/bin/python  
~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test/.venv/bin/python --version  
3.11.11  


touch hello.cpp  
touch CMakeLists.txt  

Launch CLion  
Open project  
~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test  
Select CMakeLists.txt  
Update C++ files  

mkdir -p build
cd build
cmake ..  
make  
hello.cpython-39-x86_64-linux-gnu.so  

ISSUE:  
PyBind  
sudo apt-get update  
sudo apt-get install pybind11-dev  

this installs global Pybind compatible with Python 3.9  
which is not what I want i.e.  
cat /usr/lib/cmake/pybind11/pybind11Config.cmake   

RETRY - IMPORTANT - must do this on the PyCharm  
i.e. in the Python virtual environment  3.11  
cmake -DPython3_EXECUTABLE=$(which python) ..  
make -j$(grep -c ^processor /proc/cpuinfo)  

hello.cpython-311-x86_64-linux-gnu.so  

Finally - copy the SO file into the virtual environment  
cd ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test/.venv/lib/python3.11/site-packages  
cp ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test/build/hello.cpython-311-x86_64-linux-gnu.so .  

Python complete:   



cd /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/org/03-inline-bindings/PyBind11Test/.venv/lib/python3.11/site-packages
/home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/org/03-inline-bindings/PyBind11Test/build/hello.cpython-311-x86_64-linux-gnu.so