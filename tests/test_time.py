from unittest import TestCase
from unittest import mock

from cornsnipps.time import time_ms, time_us, time_spent_from

current_time = 13.37


class TestTime(TestCase):
    @mock.patch('time.time', return_value=current_time)
    def test_time_ms(self, mock_time):
        _current_time_ms = current_time * 1000

        _time_ms = time_ms()
        self.assertEqual(int(_current_time_ms), _time_ms)
        self.assertIsInstance(_time_ms, int)

        _time_ms = time_ms(True)
        self.assertEqual(_current_time_ms, _time_ms)
        self.assertIsInstance(_time_ms, float)

    @mock.patch('time.time', return_value=current_time)
    def test_time_us(self, mock_time):
        _current_time_us = current_time * 1000 * 1000

        _time_us = time_us()
        self.assertEqual(int(_current_time_us), _time_us)
        self.assertIsInstance(_time_us, int)

        _time_us = time_us(True)
        self.assertEqual(_current_time_us, _time_us)
        self.assertIsInstance(_time_us, float)

    @mock.patch('time.time', return_value=current_time + 11.1)
    def test_time_spent_from(self, mock_time):
        self.assertAlmostEqual(11.1, time_spent_from(current_time))
