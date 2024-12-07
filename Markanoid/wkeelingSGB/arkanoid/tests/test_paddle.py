import math
from unittest import TestCase
from unittest.mock import (ANY,
                           call,
                           Mock,
                           patch)

import pygame

from arkanoid.sprites.paddle import (LaserBullet,
                                     LaserState,
                                     Paddle)


class TestPaddle(TestCase):

    @patch('arkanoid.sprites.paddle.load_png_sequence')
    @patch('arkanoid.sprites.paddle.load_png')
    @patch('arkanoid.sprites.paddle.pygame')
    def test_initialize(self, mock_pygame, mock_load_png,
                        mock_load_png_sequence):
        mock_screen, mock_area, mock_image, mock_rect = (
            Mock(), Mock(), Mock(), Mock())
        mock_screen.left = 0
        mock_screen.height = 650
        mock_screen.width = 600
        mock_rect.height = 10
        mock_pygame.Rect.return_value = mock_area
        mock_area.center = 'area center'
        mock_pygame.display.get_surface.return_value.get_rect.return_value = \
            mock_screen
        mock_load_png.return_value = mock_image, mock_rect

        paddle = Paddle(left_offset=10, right_offset=10, bottom_offset=20)

        self.assertEqual(paddle.image, mock_image)
        self.assertEqual(paddle.rect, mock_rect)
        self.assertIs(paddle.visible, True)
        mock_pygame.Rect.assert_called_once_with(10, 630, 580, 10)
        self.assertEqual(paddle.rect.center, 'area center')

    @patch('arkanoid.sprites.paddle.load_png_sequence')
    @patch('arkanoid.sprites.paddle.load_png')
    @patch('arkanoid.sprites.paddle.pygame')
    def test_update_moves_when_in_ares(self, mock_pygame, mock_load_png,
                                       mock_load_png_sequence):
        


