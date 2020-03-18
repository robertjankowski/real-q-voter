import logging


def get_logger(name: str) -> logging.Logger:
    """
    Get logger with given `name`

    :param name: Name of logger
    :return: logging.Logger
    """
    return logging.getLogger(name)
