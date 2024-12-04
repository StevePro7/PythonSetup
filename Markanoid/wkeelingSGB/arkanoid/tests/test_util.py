import os
import unittest
import unittest.mock
#import unittest.mock

import arkanoid.utils.util as util




class TestUtil(unittest.TestCase):

    def setUp(self) -> None:
        self._high_score_file = os.path.join(os.path.expanduser('~'),
                                             'arkanoid')
        self._high_score_file_backup = os.path.join(os.path.expanduser('~'),
                                             'arkanoid.bak')
        if os.path.exists(self._high_score_file):
            os.rename(self._high_score_file, self._high_score_file_backup)

    def tearDown(self) -> None:
        if os.path.exists(self._high_score_file_backup):
            os.rename(self._high_score_file, self._high_score_file_backup)

    @unittest.mock.patch('arkanoid.utils.util.pygame')
    def test_returns_left_pos_for_horizontal_centre(self, mock_pygame):
        mock_screen = unittest.mock.Mock()
        mock_screen.get_width.return_value = 600
        mock_pygame.display.get_surface.return_value = mock_screen

        mock_surface = unittest.mock.Mock()
        mock_surface.get_width.return_value = 100

        self.assertEqual(util.h_centre_pos(mock_surface), 250)

    def test_save_high_score(self):
        high_score = 1000
        util.save_high_score(high_score)

        with open(self._high_score_file) as file:
            saved_score = int(file.read().strip())
            self.assertEqual(saved_score, high_score)

    def test_loads_high_score_when_file_exists(self):
        high_score = 2000

        with open(self._high_score_file, 'w') as file:
            file.write(str(high_score))

        self.assertEqual(util.load_high_score(), high_score)

    def test_loads_high_score_when_file_not_exists(self):
        try:
            os.remove(self._high_score_file)
        except OSError:
            pass

        self.assertEqual(util.load_high_score(), 0)

