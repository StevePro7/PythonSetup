Build Your First Neural Network
21-Feb-2026

https://techwithram.medium.com/build-your-first-neural-network-57ae8697052f


mkdir -p D:\GitHub\StevePro9\PythonSetup\Medium\DL\BuildNeuralNetwork
uv init --python 3.11
uv venv --python 3.11
.venv\Scripts\activate

uv add numpy
uv lock
uv sync


TODO
Q1.
how are these the same?
z = w * x + b  
z = np.dot(self.w, x) + self.b