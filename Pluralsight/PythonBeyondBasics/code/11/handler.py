#!/usr/bin/env python3
from random import randrange

def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input("Guess? "))
        except ValueError:
            continue

        if guess == number:
            print("You win!")
            break

        if guess < number:
            print("guess higher")

        if guess > number:
            print("guess lower")


if __name__ == '__main__':
    main()