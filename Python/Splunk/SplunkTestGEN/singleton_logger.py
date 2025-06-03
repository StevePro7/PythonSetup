import logging
import json
from threading import Lock

class SingletonLogger:
    _instance = None
    _lock = Lock()
    _initialized = False

    def __init__(self, log_level):
        if self._initialized:
            return

        self.logger = logging.getLogger("microservices_logger")

        log_level_attr = getattr(logging, log_level, logging.INFO)
        self.logger.setLevel(log_level_attr)

        formatter = JSONFormatter()

        filter = RedactFilter()
        self.logger.addFilter(filter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        self._initialized = True


    @classmethod
    def instance(cls, log_level=logging.INFO):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls(log_level)
            else:
                pass
        return cls._instance

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "lineno": record.lineno,
        }
        return json.dumps(log_record)


class RedactFilter(logging.Filter):
    def filter(self, record):
        if isinstance(record.msg, str):
            # Redact sensitive information
            record.msg = record.msg.replace("password", "[REDACTED]")
            record.msg = record.msg.replace("token", "[REDACTED]")
        return True
