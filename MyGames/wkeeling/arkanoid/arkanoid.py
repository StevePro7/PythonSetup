import logging
import arkanoid.game

logging.basicConfig()
LOG = logging.getLogger("arkanoid")
LOG.setLevel(logging.DEBUG)


if __name__ == '__main__':
    game: arkanoid.game.Arkanoid = arkanoid.game.Arkanoid()
    game.main_loop()
    print('arkanoid')
