import pygame
from pygame._sdl2 import get_audio_device_names
from MyGame import MyGame
from utils import get_project_root
from pathlib import Path
import enumerations as enums

class SoundManager:
    def __init__(self):
        self.audioEnable = False
        self.musicEnable = False
        self.soundEnable = True
        self.music: dict[enums.MusicType, str] = {}
        self.sound: dict[enums.SoundType, str] = {}
        self.currMusic = None
        self.currSound = None

    def Initialize(self):
        self.audioEnable = pygame.mixer.get_init() is not None
        if self.audioEnable:
            pygame.mixer.init()
            devices = get_audio_device_names(False)
            MyGame.Manager.LogManager.Debug(devices)


    def LoadContent(self):
        if not self.audioEnable:
            return

        for type in enums.MusicType:
            file = self.GetAudioFile(type.name, "mp3")
            self.music[type] = file

        for type in enums.SoundType:
            file = self.GetAudioFile(type.name, "wav")
            sfx: pygame.mixer.Sound = pygame.mixer.Sound(file)
            self.sound[type] = sfx


        # tm = enums.SoundType.Wrong
        # sf = f"{tm.name}"
        # ex = "wav"
        # xx = self.GetAudioFile(sf, ex)
        # sfx: pygame.mixer.Sound = pygame.mixer.Sound(xx)
        # self.sound[tm] = sfx


    def PlaySound(self, type: enums.SoundType):
        if not self.soundEnable:
            return

        sfx: pygame.mixer.Sound = self.sound[type]
        self.currSound = sfx
        sfx.play()


    def PlayMusic(self, type: enums.MusicType):
        song = self.music[type]
        self.currMusic = song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

    def StopMusic(self):
        pygame.mixer.music.stop()               # adriana - test API

    def IsMusicPlaying(self) -> bool:
        return pygame.mixer.music.get_busy() and self.currMusic is not None

    def GetAudioFile(self, soundFile: str, extention: str) -> str:
        root: Path = get_project_root()
        file = f"{soundFile}.{extention}"
        path: Path = root / "Sound" / file      # adriana - hardcode Sound
        return path