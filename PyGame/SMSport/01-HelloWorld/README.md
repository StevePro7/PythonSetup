01-Hello World
24-Apr-2026

Reference:
https://steveproxna.blogspot.com/2017/09

mkdir /home/stevepro/GitHub/StevePro9/PythonSetup/PyGame/SMSport/01-HelloWorld
uv init --python 3.11
uv venv --python 3.11
uv add pygame
uv lock
uv sync

How this maps to your original code
SMS_setSpritePaletteColor(0, RGB(3,3,3));
→ We convert that to a standard RGB color and use it to fill the screen.
SMS_displayOn();
→ In Pygame, the display is effectively “on” once you create the window.
SMS_waitForVBlank();
→ clock.tick(60) approximates waiting for the next frame (~60Hz).