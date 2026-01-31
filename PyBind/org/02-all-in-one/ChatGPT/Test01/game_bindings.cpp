// game_bindings.cpp
#include <pybind11/pybind11.h>

extern "C" {
    void step_game(char direction);
}

namespace py = pybind11;

PYBIND11_MODULE(game, m) {
    m.def("step_game", &step_game, "Move the player in the game");
}
