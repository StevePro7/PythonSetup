ChatGPT01
20-Dec-2025

Reference:
https://numpy.org/doc/stable/user/quickstart.html
https://numpy.org/doc/stable/user/absolute_beginners.html

cd ~/GitHub/StevePro9/PythonSetup/AI/NumPy
uv init OfficialDocs

cd OfficialDocs/
uv venv --python 3.11.11
source .venv/bin/activate
OR
.venv\Scripts\activate

uv add numpy
uv sync

uv add matplotlib


print(hex(a.__array_interface__['data'][0]))
print(hex(b.__array_interface__['data'][0]))


Ex20
https://numpy.org/doc/stable/user/absolute_beginners.html


# How do you know the shape and size of an array?
ndim        number of dimensions [or axis]
size        total number of elements in ND array
shape       tuple along each dimension


IMPORTANT
tuple & or | are and | or


Broadcasting
execute an operation btwn an array and a single number
[i.e. vector and scalar]


More usefull array operations
data = np.array([1, 2, 3])
data.max()
# 3
data.min()
# 1
data.sum()
# 6

