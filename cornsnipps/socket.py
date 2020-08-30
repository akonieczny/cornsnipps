import socket
import logging
from typing import Union

__all__ = ['wsocket']

logger = logging.getLogger(__name__)


# noinspection PyPep8Naming
class wsocket(socket.socket):
    """Wrapper for standard socket.socket class.

    This class add some methods to socket object. Public methods and
    arguments are not been overwritten.
    """

    def recv_until(self, until: bytes, trim: bool = False,
                   recv_buffer_size: int = 1) -> Union[bytes, bool]:
        """Listen for data on the socket until receive 'wait_for' bytes.

        :param until: keep receiving data until receive these bytes
        :param trim: trim received data
        :param recv_buffer_size: size of the recv() buffer
        :return: received data or False when error occurred
        """
        data = b''

        expected_data_index = -1
        while expected_data_index == -1:
            try:
                chunk = self.recv(recv_buffer_size)
            except socket.error as msg:
                logger.error(f'Receiving failed: {msg}')
                logger.debug(f'Received data: {data}')
                return False

            data += chunk
            expected_data_index = data.find(until)

        if trim:
            data = data[:expected_data_index + len(until)]

        return data
