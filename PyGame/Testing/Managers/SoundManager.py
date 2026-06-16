import pygame
from pygame._sdl2 import get_audio_device_names
from pathlib import Path
from MyGame import MyGame
from Static import Constants as const
from Static import Enumerations as enums


class SoundManager:
    def __init__(self):
        self.audioEnable = False
        self.soundEnable = False
        self.music: dict[enums.MusicType, str] = {}
        self.sound: dict[enums.SoundType, str] = {}
        self.currMusic = None
        self.currSound = None
        self.prevSound = None
        self.volume: int = None
        self.channel: pygame.mixer.Channel = None


    def Initialize(self) -> None:
        self.audioEnable = pygame.mixer.get_init() is not None
        if self.audioEnable:
            pygame.mixer.init()
            devices = get_audio_device_names(True)
            MyGame.Manager.LogManager.Debug(devices)

            # Edge case where pygame may "detect" device but list is empty
            if len(devices) == 0:
                self.audioEnable = False
                self.soundEnable = False
            else:
                self.soundEnable = MyGame.Manager.ConfigManager.ConfigData.SoundEnable
                self.SetVolume()
        else:
            self.soundEnable = False
        self.prevSound = -1


    def LoadContent(self) -> None:
        if not self.audioEnable:
            return

        for type in enums.MusicType:
            file = self.__getAudioFile(type.name, "mp3")
            self.music[type] = file

        for type in enums.SoundType:
            file = self.__getAudioFile(type.name, "wav")
            sfx: pygame.mixer.Sound = pygame.mixer.Sound(file)
            self.sound[type] = sfx


    def PlaySound(self, type: enums.SoundType) -> None:
        if not self.audioEnable or not self.soundEnable:
            return

        sfx: pygame.mixer.Sound = self.sound[type]
        self.currSound = sfx
        self.channel: pygame.mixer.Channel = sfx.play()


    def PlayRightSound(self) -> None:
        self.PlayMultiSound(0)

    def PlayWrongSound(self) -> None:
        self.PlayMultiSound(const.WRONG_DELTA)

    def PlayMultiSound(self, delta: int = 0) -> None:
        while True:
            value = MyGame.Manager.RandomManager.Next(const.SOUND_MAXIM)
            value += delta
            if value != self.prevSound:
                self.prevSound = value
                break

        type: enums.SoundType = enums.SoundType(value)
        self.PlaySound(type)


    def PlayMusic(self, type: enums.MusicType) -> None:
        if not self.audioEnable:
            return

        song = self.music[type]
        self.currMusic = song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

    def StopMusic(self) -> None:
        if not self.audioEnable:
            return

        pygame.mixer.music.stop()

    def PauseMusic(self) -> None:
        if not self.audioEnable:
            return

        pygame.mixer.music.pause()

    def ResumeMusic(self) -> None:
        if not self.audioEnable:
            return

        pygame.mixer.music.unpause()

    def IsMusicPlaying(self) -> bool:
        if not self.audioEnable:
            return False

        return pygame.mixer.music.get_busy() and self.currMusic is not None

    def IsSoundPlaying(self) -> bool:
        if not self.audioEnable or not self.soundEnable:
            return False

        return self.channel and self.channel.get_busy() and self.currSound is not None

    def AlternateSound(self) -> None:
        self.soundEnable = not self.soundEnable
        self.SetVolume()

    def DrawVolumeIcon(self) -> None:
        if self.soundEnable:
            MyGame.Manager.SpriteManager.DrawVolumeOn()
        else:
            MyGame.Manager.SpriteManager.DrawVolumeOff()


    def SetVolume(self) -> None:
        self.volume = 1 if self.soundEnable else 0
        pygame.mixer.music.set_volume(self.volume)


    @property
    def SoundEnable(self) -> bool:
        return self.audioEnable and self.soundEnable

    def __getAudioFile(self, soundFile: str, extention: str) -> str:
        root: Path = MyGame.Manager.BaseManager.GetProjectRoot()
        file = f"{soundFile}.{extention}"
        path: Path = root / const.SOUND_DIRECTORY / file
        return path