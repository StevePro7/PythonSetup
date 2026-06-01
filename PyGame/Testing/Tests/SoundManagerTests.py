from Managers.SoundManager import SoundManager
from bootstrap import build_game
import pygame
#import enumerations as enums

registry = build_game()

pygame.init()
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


print("the end")
