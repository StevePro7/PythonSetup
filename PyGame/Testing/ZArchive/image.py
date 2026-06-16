import pygame
import random
import math


class Constants:
    NUMBER_CHARACTERS = 16
    NUMBER_SPRITES = 8

    SpriteSize = 80  # adjust if needed

    GameOffsetX = 50
    TextsSize = 32
    ScreenWide = 1280
    ScreenHigh = 720


class SpriteType:
    Select = 0
    Right = 1
    Wrong = 2
    LeftArrow = 3
    RightArrow = 4
    VolumeOn = 5
    VolumeOff = 6
    White = 7


class ActorType:
    Lisa1 = 14
    Lisa2 = 15


class ImageManager:
    def __init__(self, spritesheet_surface: pygame.Surface):
        self.spritesheet = spritesheet_surface

        self.zero_posn = (0, 0)
        self.head_posn = (0, 0)

        self.title_rect = None
        self.header_rect = None

        self.title_vect = (0, 0)
        self.header_vect = (0, 0)

        self.actor_rects = []
        self.actor_vect = (0, 0)

        self.sprite_rects = []
        self.image_rotate = 0

        self.image_wide = 240
        self.image_high = 320
        self.sprite_size = Constants.SpriteSize

        self.curr_actor = Constants.NUMBER_CHARACTERS
        self.next_actor = 0

    # -------------------------
    # Initialization
    # -------------------------
    def initialize(self):
        self.curr_actor = Constants.NUMBER_CHARACTERS
        self.next_actor = 0
        self.generate_next_actor()

    def load_content(self):
        self.zero_posn = (Constants.GameOffsetX, 0)
        self.head_posn = (Constants.GameOffsetX, Constants.TextsSize // 2)

        self.title_rect = pygame.Rect(0, 0, 2 * self.image_wide, 2 * self.image_high)
        self.title_vect = (2 * self.image_wide, 0)

        self.header_rect = pygame.Rect(
            4 * self.image_high - self.sprite_size,
            0,
            self.sprite_size,
            2 * self.image_high
        )
        self.header_vect = (self.sprite_size, 0)

        self.actor_rects = self.populate_actor_rects()

        self.actor_vect = (
            Constants.ScreenWide - self.image_wide - Constants.GameOffsetX,
            Constants.ScreenHigh - self.image_high
        )

        self.sprite_rects = self.populate_sprite_rects()

        self.image_rotate = math.radians(270)

    # -------------------------
    # Actor logic
    # -------------------------
    def generate_next_actor(self):
        while True:
            self.next_actor = random.randint(0, Constants.NUMBER_CHARACTERS - 1)
            if self.curr_actor != self.next_actor:
                break

        self.curr_actor = self.next_actor

    # -------------------------
    # Drawing helpers
    # -------------------------
    def draw_title(self, screen):
        self._draw_rotated(
            screen,
            self.title_rect,
            self.zero_posn,
            self.title_vect
        )

    def draw_header(self, screen):
        self._draw_rotated(
            screen,
            self.header_rect,
            self.head_posn,
            self.header_vect
        )

    def draw_curr_actor(self, screen):
        self.draw_actor(screen, self.curr_actor)

    def draw_next_actor(self, screen):
        self.generate_next_actor()
        self.draw_actor(screen, self.curr_actor)

    def draw_actor(self, screen, index: int):
        x, y = self.actor_vect
        scale = 1.0

        # special scaling for Lisa
        if index in (ActorType.Lisa1, ActorType.Lisa2):
            scale = 0.85
            y += 2 * Constants.TextsSize

        rect = self.actor_rects[index]
        sprite = self.spritesheet.subsurface(rect)

        if scale != 1.0:
            w = int(rect.width * scale)
            h = int(rect.height * scale)
            sprite = pygame.transform.smoothscale(sprite, (w, h))

        screen.blit(sprite, (x, y))

    def draw_sprite(self, screen, sprite_type: int, position):
        rect = self.sprite_rects[sprite_type]
        screen.blit(self.spritesheet, position, rect)

    # -------------------------
    # Internal draw (rotation like XNA)
    # -------------------------
    def _draw_rotated(self, screen, source_rect, pos, origin):
        image = self.spritesheet.subsurface(source_rect)
        rotated = pygame.transform.rotate(image, math.degrees(self.image_rotate))

        rect = rotated.get_rect()
        rect.topleft = (pos[0] - origin[0], pos[1] - origin[1])

        screen.blit(rotated, rect.topleft)

    # -------------------------
    # Rect generation
    # -------------------------
    def populate_actor_rects(self):
        rects = [None] * Constants.NUMBER_CHARACTERS

        rects[0] = self.get_actor_rect(0, 2)
        rects[1] = self.get_actor_rect(0, 3)
        rects[2] = self.get_actor_rect(1, 2)
        rects[3] = self.get_actor_rect(1, 3)

        rects[4] = self.get_actor_rect(2, 0)
        rects[5] = self.get_actor_rect(2, 1)
        rects[6] = self.get_actor_rect(2, 2)
        rects[7] = self.get_actor_rect(2, 3)

        rects[8] = self.get_actor_rect(3, 0)
        rects[9] = self.get_actor_rect(3, 1)
        rects[10] = self.get_actor_rect(3, 2)
        rects[11] = self.get_actor_rect(3, 3)

        rects[12] = self.get_actor_rect(4, 0)
        rects[13] = self.get_actor_rect(4, 1)
        rects[14] = self.get_actor_rect(4, 2)
        rects[15] = self.get_actor_rect(4, 3)

        return rects

    def get_actor_rect(self, x, y):
        return pygame.Rect(
            x * self.image_wide,
            y * self.image_high,
            self.image_wide,
            self.image_high
        )

    def populate_sprite_rects(self):
        rects = [None] * Constants.NUMBER_SPRITES

        x = 4 * self.image_high - self.sprite_size
        y = 2 * self.image_high

        rects[SpriteType.Select] = self.get_sprite_rect(x, y, 0)
        rects[SpriteType.Right] = self.get_sprite_rect(x, y, 1)
        rects[SpriteType.Wrong] = self.get_sprite_rect(x, y, 2)
        rects[SpriteType.LeftArrow] = self.get_sprite_rect(x, y, 3)
        rects[SpriteType.RightArrow] = self.get_sprite_rect(x, y, 4)
        rects[SpriteType.VolumeOn] = self.get_sprite_rect(x, y, 5)
        rects[SpriteType.VolumeOff] = self.get_sprite_rect(x, y, 6)
        rects[SpriteType.White] = self.get_sprite_rect(x, y, 7)

        return rects

    def get_sprite_rect(self, x, y, index):
        y = y + index * self.sprite_size
        return pygame.Rect(x, y, self.sprite_size, self.sprite_size)