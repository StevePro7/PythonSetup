from AnGame import AnGame


def main():
    try:
        game = AnGame()
        game.Run()
    except KeyboardInterrupt:
        game.Exit()
    finally:
        game.ShutDown()


if __name__ == "__main__":
    main()
