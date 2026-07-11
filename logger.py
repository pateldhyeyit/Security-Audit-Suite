# modules/logger.py

import logging

from config import LOG_FILE

# Create logger
logger = logging.getLogger("SecurityAuditSuite")
logger.setLevel(logging.INFO)

# Avoid adding duplicate handlers if imported multiple times
if not logger.handlers:

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def log_info(message):
    """
    Write an INFO log.
    """
    logger.info(message)
    print(f"[INFO] {message}")


def log_warning(message):
    """
    Write a WARNING log.
    """
    logger.warning(message)
    print(f"[WARNING] {message}")


def log_error(message):
    """
    Write an ERROR log.
    """
    logger.error(message)
    print(f"[ERROR] {message}")