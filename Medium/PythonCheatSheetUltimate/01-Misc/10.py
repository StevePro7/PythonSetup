# 10.  Using Argparse for Complex CLI Interactions
#  python 01-Misc/10.py spell=test
# python 01-Misc/10.py spell=test --power=10

import argparse
parser = argparse.ArgumentParser(description="Invoke the ancient scripts.")
parser.add_argument('spell', help="The spell to cast")
parser.add_argument('--power', type=int, help="The power level of the spell")
args = parser.parse_args()
print(f"Casting {args.spell} with power {args.power}")