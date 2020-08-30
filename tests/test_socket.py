import logging
import socket
from unittest import TestCase
from unittest import mock
from unittest.mock import Mock

from cornsnipps.socket import wsocket

recv_mock = lambda self, bufsize: b'ABC'
recv_mock_exception = Mock(side_effect=socket.error())


class TestExtSocket(TestCase):
    def setUp(self) -> None:
        self.socket = wsocket(socket.AF_INET, socket.SOCK_DGRAM)
        self.until = bytes('CA', 'utf-8')

        logging.disable(logging.CRITICAL)

    def tearDown(self) -> None:
        self.socket.close()

        logging.disable(logging.NOTSET)

    @mock.patch('socket.socket.recv', recv_mock)
    def test_recv_until(self):
        data = self.socket.recv_until(self.until)

        self.assertIsInstance(data, bytes)
        self.assertEqual(b'ABCABC', data)

    @mock.patch('socket.socket.recv', recv_mock)
    def test_recv_until_trim_data(self):
        data = self.socket.recv_until(self.until, trim=True)

        self.assertIsInstance(data, bytes)
        self.assertEqual(b'ABCA', data)

    @mock.patch('socket.socket.recv', Mock(side_effect=socket.error('Message')))
    def test_recv_until_recv_throw_exception(self):
        data = self.socket.recv_until(self.until)

        self.assertFalse(data)
