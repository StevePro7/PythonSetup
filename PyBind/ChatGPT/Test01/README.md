README.md
06-Jan-2025

sega master system game written in C - how can I integrate python scripts to control the game play with pybind - can you give me an example

https://chatgpt.com/c/677c41e9-33a8-8005-b688-7605c39c085b


game.c
game_bindings.cpp

g++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` game_bindings.cpp game.c -o game`python3-config --extension-suffix`
