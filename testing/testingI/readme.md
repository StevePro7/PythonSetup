readme
29-Sep-2023

https://medium.com/@abelkrw/exploring-the-art-of-generative-ai-in-python-2c15a7b54435

PyCharm
New Project
D:\GitHub\StevePro9\PythonSetup\TestGenAI
Virtual environment	venv

import tensorflow as tf
Module Not Found

Follow instruction here
https://stackoverflow.com/questions/41415629/importerror-no-module-named-tensorflow-python

cd venv\Scripts
activate
pip3 install tensorflow


Tensorflow
SSE
Streaming SIMD Extensions

SIMD
Single Instruction Multiple Data



ERROR
2.13.1
Traceback (most recent call last):
  File "/home/stevepro/GitHub/StevePro9/PythonSetup/testing/main.py", line 30, in <module>
    vae_outputs = decoder(encoder(encoder_inputs))
  File "/home/stevepro/GitHub/StevePro9/PythonSetup/testing/venv/lib/python3.8/site-packages/keras/src/utils/traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "/home/stevepro/GitHub/StevePro9/PythonSetup/testing/venv/lib/python3.8/site-packages/keras/src/engine/input_spec.py", line 280, in assert_input_compatibility
    raise ValueError(
ValueError: Exception encountered when calling layer "decoder" (type Functional).

Input 0 of layer "dense_1" is incompatible with the layer: expected axis -1 of input shape to have value 64, but received input with shape (None, 128)

Call arguments received by layer "decoder" (type Functional):
  • inputs=tf.Tensor(shape=(None, 128), dtype=float32)
  • training=None
  • mask=None

Process finished with exit code 1
