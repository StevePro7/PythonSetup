PyBind11TestProject  
06-Dec-2025  

cd ~/GitHub/StevePro9/PythonSetup/PyBind  
mkdir PyBind11TestProject  
cd PyBind11TestProject  
touch README.md  

mkdir Cpp  
mkdir Python  
touch CMakeLists.txt 
setup directory structure  
Launch CLion  
Open ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11TestProject  
COMPLETE all C++ code  
Build + run Tests  

Launch PyCharm  
Open ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11TestProject/Python  
uv init --python 3.11.11  
#uv venv --python 3.11.11  
source .venv/bin/activate  
uv add pybind11  
uv sync  

Update Python code  

CLion  
mkdir -p build
cd build  

PyCharm  
cd ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11TestProject/build  
cmake -DPython3_EXECUTABLE=$(which python) ..  
make -j$(grep -c ^processor /proc/cpuinfo)  
myproject.cpython-311-x86_64-linux-gnu.so  

PyCharm  
Finally - copy the SO file into the virtual environment    
cd ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11TestProject/Python/.venv/lib/python3.11/site-packages  
cp ~/GitHub/StevePro9/PythonSetup/PyBind/PyBind11TestProject/build/Cpp/myproject.cpython-311-x86_64-linux-gnu.so .
