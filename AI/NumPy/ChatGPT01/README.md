ChatGPT01
20-Dec-2025

Reference:
https://chatgpt.com/c/69469fff-76d8-832c-b10b-2e8f1561f3a1

cd ~/GitHub/StevePro9/PythonSetup/AI/NumPy
uv init ChatGPT01

cd ChatGPT01/
uv venv --python 3.11.11
source .venv/bin/activate

uv add numpy


NUMPY
N-dimensional array library
Vectorized loops    No Python loops
Foundation
- PyTorch
- TensorFlow
- scikit-learn
- JAX     Python library for accelerator-oriented array computation and program transformation


Ex01        What NumPy Is
numpy


Ex02        Arrays (ndarray)
ndarray ND = number dimensions
dtype   data type
ndim    N-dimensions of ndarray


Ex03        Common Constructors
eye         identity matrix N = number rows
arange      start, stop, step   >=start, <stop
linspace    start, stop, num    number of intervals >=start && <=stop
rand        +ve random +0 to +1
randn       -ve random -1 to +1


Ex04        Indexing & Slicing
x[1:3]      >=start && <stop


Ex05        Boolean Masking (Critical for ML)
x > 2       greater than


Ex06        Vectorized Operations (No Loops)
this is why NumPy is fast


Ex07        Broadcasting (VERY IMPORTANT)
mechanism that allows NumPy to perform arithmetic 
operations on arrays of different shapes + sizes

dimensions alight from right
size 1 can stretch


