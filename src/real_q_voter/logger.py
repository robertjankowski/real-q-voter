import logging


def get_logger(name: str) -> logging.Logger:
    """
    Get logger with given `name`

    :param name: Name of logger
    :return: logging.Logger
    """
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger
