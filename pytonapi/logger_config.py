import logging
from logging import Logger


def setup_logging(debug: bool = False) -> Logger:
    """
    Set up the logging configuration for the application.

    :param debug: Boolean flag to enable debug logging. If True, sets the logging level to DEBUG; otherwise, INFO.
    :return: The configured logger instance.
    """
    logger = logging.getLogger("pytonapi")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    httpx_logger = logging.getLogger("httpx")
    httpx_logger.setLevel(logging.WARNING)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG if debug else logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
