import logging
import sys


class LogFilter(logging.Filter):
    """Filters (lets through) all messages with level < LEVEL"""
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno < self.level


# создадим обработчики для сообщений и для ошибок
stdout_handler = logging.StreamHandler(sys.stdout)
stderr_handler = logging.StreamHandler(sys.stderr)

# добавим фильтр, чтобы разные уровни попадали в разные обработчики
log_filter = LogFilter(logging.WARNING)
stdout_handler.addFilter(log_filter)
stdout_handler.setLevel(logging.DEBUG)
stderr_handler.setLevel(logging.WARNING)

rootLogger = logging.getLogger()
rootLogger.addHandler(stdout_handler)
rootLogger.addHandler(stderr_handler)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
