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

python hello.py