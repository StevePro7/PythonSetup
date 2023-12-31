import argparse
import retro

parser = argparse.ArgumentParser()
parser.add_argument('--game', default='SonicTheHedgehog-Genesis', help='the name or path for the game to run')
parser.add_argument('--state', help='the initial state file to load, minus the extension')
parser.add_argument('--scenario', '-s', default='scenario', help='the scenario file to load, minus the extension')
parser.add_argument('--record', '-r', action='store_true', help='record bk2 movies')
parser.add_argument('--verbose', '-v', action='count', default=1, help='increase verbosity (can be specified multiple times)')
parser.add_argument('--quiet', '-q', action='count', default=0, help='decrease verbosity (can be specified multiple times)')
parser.add_argument('--obs-type', '-o', default='image', choices=['image', 'ram'], help='the observation type, either `image` (default) or `ram`')
parser.add_argument('--players', '-p', type=int, default=1, help='number of players/agents (default: 1)')
args = parser.parse_args()

print('beg')
print(args.state)
#print(retro.State.DEFAULT)
print('end')

env = retro.make(game='SonicTheHedgehog2-Genesis', state='HillTopZone.Act1')
env.reset()
env.render()