from unittest import TestCase
from unittest import mock

from cornsnipps.time import time_ms, time_us


class TestTime(TestCase):
    @mock.patch('time.time', return_value=1337)
    def test_time_ms(self, mock_time):
        self.assertEqual(1337 * 1000, time_ms())

    @mock.patch('time.time', return_value=1337)
    def test_time_us(self, mock_time):
        self.assertEqual(1337 * 1000 * 1000, time_us())
