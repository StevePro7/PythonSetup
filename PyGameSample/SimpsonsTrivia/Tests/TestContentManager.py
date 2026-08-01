from Game.Static.Assets import Assets


def test_load_content(baseManager, pyGameManager, contentManager):
    baseManager.Initialize()
    pyGameManager.Initialize()

    contentManager.Initialize()
    contentManager.LoadContent()

    assert Assets.SplashTexture is not None
    assert Assets.SplashTexture.get_width() == 384
    assert Assets.SplashTexture.get_height() == 256
