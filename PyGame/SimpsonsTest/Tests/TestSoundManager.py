# import Game.Static.Enumerations as enums
# from Game.Managers.SoundManager import SoundManager


def test_play_music(baseManager, pyGameManager, configManager, randomManager, soundManager):
    baseManager.Initialize()
    pyGameManager.Initialize()
    configManager.Initialize()
    randomManager.Initialize()

    soundManager.Initialize()
    soundManager.LoadContent()

    # soundManager.PlayRightSound()
    # soundManager.PlayWrongSound()

    # soundManager.PlayMusic(enums.MusicType.TitleMusic))
    # soundManager.PlayMusic(enums.MusicType.HappyMusic))

