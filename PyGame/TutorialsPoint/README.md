TutorialsPoint
04-Apr-2026

Reference:
anLinks02.txt
/home/stevepro/GitHub/StevePro10/Blogger/Python/PyGame

https://www.tutorialspoint.com/pygame/pygame_tutorial.pdf

pygame_tutorial.pdf
/home/stevepro/Steven/Books/Python


cd ~/GitHub/StevePro9/PythonSetup 
mkdir PyGame && cd PyGame
mkdir TutorialsPoint && cd TutorialsPoint
uv init --python 3.11
Initialized project `tutorialspoint`
uv venv --python 3.11
source .venv/bin/activate

uv add pygame
uv add numpy


Chp01.
PyGame
cross-platform wrapper around SDL [Simple DirectMedia Library]


Chp02.
event queue


Chp03.
set_mode() = display surface


Chp04.
canvas.fill((0, 0, 0))


Chp05.
color alpha=255 = fully opaque


Chp06.
pygame.event.EventType


Chp07.
KEYUP and KEYDOWN events
pygame.key
get_pressed
name
key_code


Chp08.
MOUSEMOTION
MOUSEBUTTONUP
MOUSEBUTTONDOWN
pygame.mouse
get_pressed
get_pos

pygame
SYSTEM_CURSOR_ARROW
SYSTEM_CURSOR_IBEAM
SYSTEM_CURSOR_WAIT
SYSTEM_CURSOR_CROSSHAIR


Chp09.
rect, circle, ellipse, polygon


Chp10.
image
loaded as a Surface object
rendered on pygame display

use Surface.blit() to render image
Surface module has convert() = optimize image format = make drawing easier


Chp11.
display text = font object = SysFont()
pygame.font.module

font object = font file = *.ttf extension
bold()
italic()
underline()


Chp12.
move an image with arrow keys


Chp13.
move an image diagonally with numeric keys


Chp14.
move an image with mouse = mouse.get_pos()


Chp15.
move_ip()       move in-place
contains()
colliderect()


Chp16.  Button
text or image surface as button - click = fire action
use collidepoint() to identify button clicked


Chp17.
pygame.transform
defintions for manipulations of Surface objects
e.g.
rotozoom        filtered scale and rotation
laplacian       extracts outline of surface object


Chp18. sound + music
pygame.mixer module


Chp19.
sound object played on specific channel instead of default channel


Chp20.

Chp26.
uv add pyopengl


Chp27.
pygame.error
raised when pygame or SDL operation fails
set_error(error_msg)
get_error()

