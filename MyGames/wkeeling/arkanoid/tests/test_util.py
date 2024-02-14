import os
import unittest
from unittest.mock import Mock
from unittest.mock import patch

import arkanoid.utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self._high_score_file = os.path.join(os.path.expanduser('~'), '.arkanoid')
        self._high_score_file_backup = os.path.join(os.path.expanduser('~'), '.arkanoid.bak')

        if os.path.exists(self._high_score_file):
            os.rename(self._high_score_file, self._high_score_file_backup)

    def tearDown(self):
        if os.path.exists(self._high_score_file_backup):
            os.rename(self._high_score_file_backup, self._high_score_file)

    @patch('arkanoid.utils.util.pygame')
    def test_returns_left_pos_for_horizontal_centre(self, mock_pygame):
        mock_screen = Mock()
        mock_screen.get_width.return_value = 600

