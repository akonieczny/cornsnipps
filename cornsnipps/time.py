import time
import typing as tp

__all__ = ['time_ms', 'time_us']


def time_ms(as_float: bool = True) -> tp.Union[int, float]:
    """Convert current time to milliseconds.

    :param as_float: result should be float, default result is int
    :return: current time in milliseconds
    """
    _time_ms = time.time() * 1000
    if not as_float:
        return _time_ms
    return int(_time_ms)


def time_us(as_float: bool = False) -> tp.Union[int, float]:
    """Convert current time to microseconds.

    Base on the time.time() instead the time.time_ns() for backward
    compatibility.

    :param as_float: result should be float, default result is int
    :return: current time in microseconds
    """
    _time_us = time.time() * 1000000
    if not as_float:
        return _time_us
    return int(_time_us)
