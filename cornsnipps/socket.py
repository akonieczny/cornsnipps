import socket
import logging

__all__ = ['wsocket']

logger = logging.getLogger(__name__)


# noinspection PyPep8Naming
class wsocket(socket.socket):
    """Wrapper for standard socket.socket class.

    This class add some methods to socket object. Public methods and
    arguments are not been overwritten.
    """
