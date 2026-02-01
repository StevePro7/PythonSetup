PyBind11Test
01-Feb-2025

cd ~/GitHub/StevePro9/PythonSetup/PyBind  
mkdir -p PyBind11Test  
uv init --python 3.11.11  
uv venv --python 3.11.11

IMPORTANT - everything is done in PyCharm - i.e. NO CLion

Launch PyCharm  
Open project  
~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test    

Creates .venv  
Otherise  
source .venv/bin/activate  

uv add pybind11
uv sync  

`which python` --version  
3.11.11  


touch hello.cpp  
touch CMakeLists.txt  

mkdir -p build
cd build
cmake -DPython3_EXECUTABLE=$(which python) ..  
make -j$(grep -c ^processor /proc/cpuinfo)  

hello.cpython-311-x86_64-linux-gnu.so  

Finally - copy the SO file into the virtual environment  
#cd ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test/.venv/lib/python3.11/site-packages  
#cp ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11Test/build/hello.cpython-311-x86_64-linux-gnu.so .  

cd /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/org/03-inline-bindings/PyBind11Test/.venv/lib/python3.11/site-packages
/home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/org/03-inline-bindings/PyBind11Test/build/hello.cpython-311-x86_64-linux-gnu.so


Python complete:
uv run main.py

OR
Set interpreter
Debug main.py