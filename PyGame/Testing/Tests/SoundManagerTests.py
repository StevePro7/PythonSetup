from Managers.SoundManager import SoundManager
from Managers.ConfigManager import ConfigManager
from Managers.RandomManager import RandomManager
from bootstrap import build_game
import pygame


registry = build_game()

pygame.init()
configManager = registry.get(ConfigManager.__name__)
configManager.Initialize()
configManager.LoadContent()

randomManager = registry.get(RandomManager.__name__)
randomManager.Initialize()

soundManager = registry.get(SoundManager.__name__)
soundManager.Initialize()
soundManager.LoadContent()

# MUSIC
#soundManager.PlayMusic(enums.MusicType.HappyMusic)
#soundManager.PlayMusic(enums.MusicType.TitleMusic)
#test: bool = soundManager.IsMusicPlaying()

# SOUND
# right = 0   # 0-2 or 3
# sfx = list(enums.SoundType)[right]
# soundManager.PlaySound(sfx)

# wrong = 6
# sfx = list(enums.SoundType)[wrong]
# soundManager.PlaySound(sfx)

#soundManager.PlaySound(enums.SoundType.Cheat)
#soundManager.PlaySound(enums.SoundType.Ready)

# soundManager.PlayRightSound()
# soundManager.PlayRightSound()
# soundManager.PlayRightSound()

soundManager.PlayWrongSound()
soundManager.PlayWrongSound()
soundManager.PlayWrongSound()

print("the end")
