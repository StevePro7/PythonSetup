import logging
import math
import random

import pygame

from arkanoid.utils.util import load_png

LOG = logging.getLogger(__name__)

TWO_PI = math.pi * 2
HALF_PI = math.pi / 2

# A value will be chosen at random between this and it's negative
# to apply to the angle of bounce for top/bottom/side collisions of the ball.
RANDOM_RANGE = 0.1  # Radians


class Ball(pygame.sprite.Sprite):
    """The ball that bounces around the screen.

    A Ball is aware of the screen, and any sprites on the screen
    that have been added via add_collidable_sprite(). Note that the game
    edges are considered to be collidable sprites.

    The ball will begin its journey using the position and angle specified
    when the ball is initialised. As the ball collides with sprites, its
    angle of bounce will be calculated. Furthermore, its speed may increase
    or decrease but it will never exceed the top_speed.
    When not colliding, the ball will gradually try to settle back to the
    base_speed.

    Once the ball goes off the screen, the no-args off_screen_callback will
    be invoked, if one was set when the ball was initialised.

    See __init__() for further information.
    """

    def __init__(self, start_pos, start_angle, base_speed, top_speed=15,
                 normalisation_rate=0.02,
                 off_screen_callback=None):
        """
        Initialise a new Ball with the given arguments.

        If supplied, the off_screen_callback will be invoked whenever the
        ball leaves the screen. This callable takes a single argument: the
        ball sprite instance.

        Args:
            start_pos:
                The starting coordinates of the ball. A 2 element sequence.
            start_angle:
                The starting angle of the ball in radians.
            base_speed:
                The baseline speed of the ball. Collisions with objects may
                momentarily increase/decrease the speed of the ball, but the
                ball will always try to gradually settle back to the base
                speed.
            top_speed:
                The maximum permitted speed of the ball. Collisions with
                objects may increase the speed of the ball, but the speed
                will never go above the top_speed.
            normalisation_rate:
                The per-frame rate at which the ball is brought back to base
                speed, should the speed have changed due to collision with
                an object.
            off_screen_callback:
                A callable that will be called if the ball goes off the edge
                of the screen. It takes a single argument: the ball sprite
                instance.
        """
        super().__init__()
        self.image, self.rect = load_png('ball')
        self.rect.x, self.rect.y = start_pos
        self.visible = True
        self.speed = base_speed
        self.base_speed = base_speed
        self.normalisation_rate = normalisation_rate
        self.angle = start_angle

        self._start_pos = start_pos
        self._start_angle = start_angle
        self._top_speed = top_speed
        self._off_screen_callback = off_screen_callback
        self._anchor = None

        # The area within which the ball is in play.
        screen = pygame.display.get_surface()
        self._area = screen.get_rect()

        # The sprites the ball can collide with.
        self._collidable_sprites = pygame.sprite.Group()

        # The actions associated with the collidable sprites.
        # This dictionary is keyed by the collidable sprite. The value is
        # a 3-element tuple corresponding to the bounce strategy, speed
        # adjustment and collision callback for that sprite.
        self._collision_data = {}

    def add_collidable_sprite(self, sprite, bounce_strategy=None,
                              speed_adjust=0.0, on_collide=None):
        """Add a sprite that the ball might collide with.

        A bounce strategy can be supplied to override the default bouncing
        behaviour of the ball whenever it strikes the sprite being added.
        The strategy should be a callable that will receive two arguments:
        the Rect of the sprite being struck, and the Rect of the ball. It
        should return the angle of bounce in radians. The angle is measured
        clockwise from the righthand x-axis. Angles should be positive.
        If not supplied, the ball will conform to normal trignometric rules
        when bouncing off the sprite.

        In addition, an optional collision callable can be supplied. This will
        be invoked to perform an action whenever the ball strikes the sprite.
        The callable takes two arguments: the sprite that the ball struck and
        the ball that struck it.

        Args:
            sprite:
                The collidable sprite.
            bounce_strategy:
                Optional callable that determines how the ball should bounce
                when it collides with the sprite. It takes 2 arguments: the
                Rect of the object and the Rect of the ball.
            speed_adjust:
                Optional numeric value that will be used to speed up or slow
                down the the ball. Use a negative value to slow the ball down.
            on_collide:
                Optional callable that will be called when a collision occurs.
                It takes 2 arguments: the sprite the ball struck and the ball
                that struck it.
        """
        self._collidable_sprites.add(sprite)
        self._collision_data[sprite] = (
            bounce_strategy, speed_adjust, on_collide)

    def remove_collidable_sprite(self, sprite):
        """Remove a sprite so that the ball can no longer collide with it.

        If the ball does not already know about the sprite, this method will
        just return without doing anything.

        Args:
            sprite:
                The collidable sprite to remove.
        """
        self._collidable_sprites.remove(sprite)
        try:
            del self._collision_data[sprite]
        except KeyError:
            pass

    def remove_all_collidable_sprites(self):
        """Remove all collidable sprites from the ball."""
        self._collidable_sprites.empty()
        self._collision_data.clear()

    def clone(self, **kwargs):
        """Clone the ball creating a new ball with the same collidable
        sprites as the instance being cloned.

        Because the collidable sprites are shared amongst the ball clones,
        when one ball hits a sprite the other balls know about it.

        This method accepts an optional list of keyword arguments. These, if
        supplied, will override the values of the ball being cloned.

        Args:
            kwargs:
                Optional keyword arguments that will be passed to the
                initialiser of the cloned ball overriding the values of the
                ball being cloned.
        """
        start_pos = kwargs.get('start_pos', self._start_pos)
        start_angle = kwargs.get('start_angle', self._start_angle)
        base_speed = kwargs.get('base_speed', self.base_speed)
        top_speed = kwargs.get('top_speed', self._top_speed)
        normalisation_rate = kwargs.get('normalisation_rate',
                                        self.normalisation_rate)
        off_screen_callback = kwargs.get('off_screen_callback',
                                         self._off_screen_callback)

        ball = Ball(start_pos, start_angle, base_speed, top_speed,
                    normalisation_rate, off_screen_callback)

        for sprite in self._collidable_sprites:
            bounce_strategy, speed_adjust, on_collide = self._collision_data[
                sprite]
            ball.add_collidable_sprite(sprite, bounce_strategy, speed_adjust,
                                       on_collide)

        return ball

    def update(self):
        pass


    def _calc_new_pos(self):
        if self._anchor:
            pos, rel_pos = self._anchor
            try:
                rect = pos.rect
            except AttributeError:
                # A fixed position.
                return pygame.Rect(pos, (self.rect.width, self.rect.height))
            # We're anchored to another sprite.
            if rel_pos:
                # Use the relative position from the sprite's left/top.
                return pygame.Rect(rect.left + rel_pos[0],
                                   rect.top + rel_pos[1], self.rect.width,
                                   self.rect.height)
            # Use the centre of the sprite.
            return rect.center
        else:
            # Move the ball normally based on angle and speed.
            offset_x = self.speed * math.cos(self.angle)
            offset_y = self.speed * math.sin(self.angle)

            return self.rect.move(offset_x, offset_y)
