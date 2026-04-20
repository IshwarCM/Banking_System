import logging
import os

def setup_logger(filename: str):
    # Use filename as logger name
    logger_name = os.path.splitext(os.path.basename(filename))[0]

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler(filename)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger