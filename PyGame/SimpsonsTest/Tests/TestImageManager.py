from Game.Static import Constants as const


def test_image_get_current_actor(baseManager, randomManager, imageManager):
    baseManager.Initialize()
    randomManager.Initialize()

    imageManager.Initialize()
    imageManager.LoadContent()

    value = imageManager.GetCurrActor
    assert value == const.NUMBER_CHARACTERS
