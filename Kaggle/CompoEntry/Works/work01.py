from Steps.step01 import Step01
import os
import sys

def work():
    #ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath: str = "../data.csv"

    step: Step01 = Step01()
    step.read_csv(filepath)

if __name__ == '__main__':
    work()