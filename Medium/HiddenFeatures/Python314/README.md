Python 3.14: Seven Cool New Features You Should Know
12-Jul-2025

https://mskadu.medium.com/python-3-14-seven-cool-new-features-you-should-know-0a79e6afaae5

01.	Template String Literals (t-strings)
02.	Enhanced Error Messages with Suggestions
03.	Improved Pattern Matching with Guard Expressions
04.	Per-Interpreter GIL Control
05.	Enhanced Type Hints with ReadOnly and TypeIs
06.	Native Zstandard Compression Support
07.	External Debugger Interface


TESTING
pyenv
# Install pyenv (Mac/Linux)
curl https://pyenv.run | bash

# Follow instructions to update your shell config (.bashrc, .zshrc, etc)

# Restart your terminal, then:
pyenv install 3.14.0b3       # replace with the latest 3.14 beta
pyenv global 3.13.5          # keep your default version
pyenv shell 3.14.0b3         # temporarily switch to 3.14 in this shell


Docker
docker run -it python:3.14-rc bash

OR
mkdir ~/python314-test
cd ~/python314-test

echo 'print("Hello from mounted folder!")' > hello.py

docker run -it --rm \
  -v "$HOME/python314-test":/app \
  -w /app \
  python:3.14-rc bash


docker run -it --rm -v "$HOME/python314-test":/app -w /app python:3.14-rc bash

python hello.py


EXAMPLES
01.
root@4ced01c039a5:/app# python hello.py
AttributeError: 'string.templatelib.Template' object has no attribute 'substitute'

02.
root@4ced01c039a5:/app# python hello.py
name 'user_list' is not defined

03.
root@4ced01c039a5:/app# python hello.py
'DatabaseConnection' object has no attribute 'execute_querry'

04.
root@4ced01c039a5:/app# python hello.py
API GET request to /api/users
Large POST request - processing with worker queue
Small POST request - processing immediately
Modifying operation: DELETE on /users/123

05.
root@4ced01c039a5:/app# python hello.py
Created user: {'id': 123, 'username': 'john_doe', 'email': 'john@example.com', 'last_login': '2024-10-15'}

06.
root@4ced01c039a5:/app# python hello.py
Original size: 41,000 bytes
Zstandard: 61 bytes (0.0001s)
Gzip: 199 bytes (0.0002s)
High compression: 61 bytes
Fast compression: 61 bytes

06.
root@4ced01c039a5:/app# python hello.py
External debugger interface not available in this Python version