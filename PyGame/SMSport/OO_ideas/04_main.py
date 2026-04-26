if __name__ == "__main__":
    game = Game()

    trivia = TriviaScene(game)
    game.set_scene(trivia)

    game.run()  