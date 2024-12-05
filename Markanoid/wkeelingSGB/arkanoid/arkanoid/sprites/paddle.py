import itertools
import logging
import math

import pygame

import arkanoid.event as event
import arkanoid.utils.util as util


LOG = logging.getLogger(__name__)


class Paddle(pygame.sprite.Sprite):
    """The movable paddle (a.k.a the "Vaus") used to control the ball to
    prevent it from dropping off the bottom of the screen."""

    def __init__(self, left_offset=0, right_offset=0, bottom_offset=0,
                 speed=10):
        """
        Create a new Paddle instance.

        The paddle will travel the entire width of the screen, unless the
        left and right offsets are specified which can restrict its travel.
        A bottom offset can also be supplied which defines how far from the
        bottom of the screen the paddle floats.

        Args:
            left_offset:
                Optional offset in pixels from the left of the screen that
                will restrict the maximum travel of the paddle.
            right_offset:
                Optional offset in pixels from the right of the screen that
                will restrict the maximum travel of the paddle.
            bottom_offset:
                The distance the paddle sits above the bottom of the screen.
            speed:
                Optional speed of the paddle in pixels per frame.
        """
        super().__init__()

        # The speed of the paddle movement in pixels per frame.
        self.speed = speed

        # The current movement in pixels. A negative value will trigger the
        # paddle to move left, a positive value to move right.
        self._move = 0

        # This toggles visibility of the paddle.
        self.visible = True

        # Load the default paddle image.
        self.image, self.rect = util.load_png('paddle')

        # Create the area the paddle can move laterally in.
        screen = pygame.display.get_surface().get_rect()
        self.area = pygame.Rect(screen.left + left_offset,
                                screen.height - bottom_offset,
                                screen.width - left_offset - right_offset,
                                self.rect.height)
        # Position the paddle.
        self.rect.center = self.area.center

        # A list of no-args callables that will be called on ball collision.
        self.ball_collide_callbacks = []

        # The current paddle state.
        self._state = NormalState(self)
# TODO
    def update(self):
        """Update the state of the paddle."""

        # Delegate to our active state for specific animation/behaviour.
        self._state.update()




    def _area_contains(self, newpos):
        return self.area.collidepoint(newpos.midleft) and \
               self.area.collidepoint(newpos.midright)


class PaddleState:
    """A PaddleState represents a particular state of the paddle, in terms
    of its graphics and behaviour.

    This base class is abstract and concrete sub-states should implement
    the update() abstract method. The update() method is called repeatedly
    by the game and is where much of the state specific logic should reside,
    such as animation.

    The enter() and exit() methods are called when the state is entered and
    exited respectively.

    When the enter() method is called, any previous paddle state is
    guaranteed to have exited. The enter() method can therefore be used to
    access any paddle attributes required for sub-state initialisation. Do
    not use __init__() for this, because a previous paddle state may still
    be in play and you may end up with attribute values you weren't expecting.

    The exit() method is called before a transition to a new state. States
    should perform any exit behaviour here, such as triggering an animation
    to return to normal, before calling the no-args on_exit callback passed
    to the exit() method.
    """

    def __init__(self, paddle):
        """Initialise the PaddleState with the paddle instance.

        The paddle instance is made available as an instance level attribute
        and can be accessed by concrete sub-states to change paddle attriubtes.

        Args:
            paddle:
                The Paddle instance.
        """
        self.paddle = paddle
        LOG.debug('Initialised {}'.format(type(self).__name__))

    def enter(self):
        """Perform any initialisation when the state is first entered."""
        pass

    def update(self):
        """Update the state of the paddle.

        Sub-states must implement this to perform state specific behaviour.
        This method is designed to be called repeatedly.
        """
        raise NotImplementedError('Subclasses must implement update()')

    def exit(self, on_exit):
        """Trigger any state specific exit behaviour before calling the no-args
        on_exit callable.

        Args:
            on_exit:
                A no-args callable that will be called when the exit behaviour
                has completed.
        """
        on_exit()

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r})'.format(class_name, self.paddle)


class NormalState(PaddleState):
    """This represents the default appearance of the paddle."""

    def __init__(self, paddle):
        super().__init__(paddle)

        self._pulsator = _PaddlePulsator(paddle, 'paddle_pulsate')

    def enter(self):
        """Set the default paddle graphic."""
        pos = self.paddle.rect.center
        self.paddle.image, self.paddle.rect = util.load_png('paddle')
        self.paddle.rect.center = pos

    def update(self):
        """Pulsate the paddle lights."""
        self._pulsator.update()



class _PaddlePulsator:
    """Helper class for pulsating the lights at the end of the paddle."""

    def __init__(self, paddle, image_sequence_name):
        """Initialise with the name of the image sequence corresponding to
        each pulsating paddle frame.

        Args:
            paddle:
                The paddle.
            image_sequence_name:
                The name of theimage sequence representing each pulsating
                frame.
        """
        self._paddle = paddle
        self._image_sequence = util.load_png_sequence(image_sequence_name)
        self._animation = None
        self._update_count = 0

    def update(self):
        """Update the paddle and pulsate the lights."""
        if self._update_count % 80 == 0:
            self._animation = itertools.chain(self._image_sequence,
                                              reversed(self._image_sequence))
            self._update_count = 0
        elif self._animation:
            try:
                if self._update_count % 4 == 0:
                    self._paddle.image, _ = next(self._animation)
            except StopIteration:
                self._animation = None

        self._update_count += 1
