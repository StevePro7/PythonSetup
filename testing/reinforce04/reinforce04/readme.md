openai retro tutorial
28-Dec-2023

LINUX
https://analyticsindiamag.com/hands-on-guide-reinforcement-learning-openai-gymretro

import retro
pip3 install gym-retro

LINUX installed OK

env = retro.make(game='Airstriker-Genesis', record='.')
AttributeError: module 'gym.utils.seeding' has no attribute 'hash_seed'

env = retro.make(game='Strider-Genesis')
AttributeError: module 'gym.utils.seeding' has no attribute 'hash_seed'

python3 -m retro.import /path/to/your/ROMs/directory/
python3 -m retro.import /home/stevepro/SEGA/ROMs/

Importing Strider-Genesis
Imported 1 games

AttributeError: module 'gym.utils.seeding' has no attribute 'hash_seed'


SOLUTION?
https://stackoverflow.com/questions/73710249/openai-gym-retro-error-attributeerror-module-gym-utils-seeding-has-no-attri

pip install gym==0.25.2