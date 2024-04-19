#!/usr/bin/python

import os

def print_hi(name: str):
    print(f"Hello, '{name}'")


if __name__ == '__main__':
    name: str = "stevepro"
    name: str = os.getenv('TEST_INPUT')
    print_hi(name)
