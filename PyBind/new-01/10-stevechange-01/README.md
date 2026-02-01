


Reference
~/GitHub/StevePro9/PythonSetup/PyBind/org/03-inline-bindings/PyBind11Test

Try similar setup for that project here

cd /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/new-01
mkdir 10-stevechange-01
cd 10-stevechange-01

uv init --python 3.11.11
uv venv --python 3.11.11
source .venv/bin/activate

uv add pybind11
uv sync  

Launch PyCharm
mkdir ThirdPartyLib
cd ThirdPartyLib
git clone https://github.com/pybind/pybind11.git 
cd ..

mkdir source
cd source
touch example.cpp
cd ..

touch CMakeLists.txt
mkdir -p build
cd build
cmake -DPython3_EXECUTABLE=$(which python) ..  
make -j$(grep -c ^processor /proc/cpuinfo)  


CMake Warning:
  Manually-specified variables were not used by the project:

    Python3_EXECUTABLE

example.cpython-311-x86_64-linux-gnu.so

Finally - copy the SO file into the virtual environment  
cd ~/GitHub/StevePro9/PythonSetup/PyBind/new-01/10-stevechange-01/.venv/lib/python3.11/site-packages  
cp /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/new-01/10-stevechange-01/build/example.cpython-311-x86_64-linux-gnu.so .