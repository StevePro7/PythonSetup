Farma Git repo
04-Aug-2024

New project
FarmaRepo
~/GitHub/StevePro9/PythonSetup/NewOpenAI

source bin activate

copy FF docs requirements.txt local
pip install -r requirements.txt
pip install --upgrade pip

GENERIC
pip install gymnasium
gymnasium==0.29.1

ClassicControl
https://gymnasium.farama.org/environments/classic_control

ToyText
https://gymnasium.farama.org/environments/toy_text

Box2D
https://gymnasium.farama.org/environments/box2d
pip install Box2D

muJoCo
https://gymnasium.farama.org/environments/mujoco
pip install mujoco==2.3.0

Atari
https://gymnasium.farama.org/environments/atari
pip install gymnasium[atari]
pip install gymnasium[accept-rom-license]