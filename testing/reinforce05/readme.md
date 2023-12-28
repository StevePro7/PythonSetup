openai retro tutorial
28-Dec-2023

PyCharm | New project   see pic

LINUX
https://analyticsindiamag.com/hands-on-guide-reinforcement-learning-openai-gymretro

import retro
ERROR

#pip3 install gym==0.25.2
pip3 install gym==0.21.0
pip3 install gym-retro

NB: at time of this writing gym-retro = 0.8.0 = latest

IMPORTANT - see why downgraded gym twice:
01.   AttributeError: module 'gym.utils.seeding' has no attribute 'hash_seed'
https://stackoverflow.com/questions/73710249/openai-gym-retro-error-attributeerror-module-gym-utils-seeding-has-no-attri

02.   ModuleNotFoundError: No module named 'gym.envs.classic_control.rendering'
https://stackoverflow.com/questions/73710249/openai-gym-retro-error-attributeerror-module-gym-utils-seeding-has-no-attri


Reference
https://stackoverflow.com/questions/73710249/openai-gym-retro-error-attributeerror-module-gym-utils-seeding-has-no-attri

LINUX installed OK

env = retro.make(game='Strider-Genesis')
      raise FileNotFoundError('Game not found: %s. Did you make sure to import the ROM?' % game)

python3 -m retro.import /path/to/your/ROMs/directory/
python3 -m retro.import /home/stevepro/SEGA/ROMs/

Importing Strider-Genesis
Imported 1 games

COMPLETE


env.render()
ModuleNotFoundError: No module named 'gym.envs.classic_control.rendering'

SOLUTION??
https://stackoverflow.com/questions/71973392/importerror-cannot-import-rendering-from-gym-envs-classic-control
pip3 install gym==0.21.0