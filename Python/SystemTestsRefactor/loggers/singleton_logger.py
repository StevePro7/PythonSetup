import logging



from threading import Lock

class SingletonLogger:
    """

    """
    _instance = None
    _lock = Lock()
    _initialized = False

    def __init__(self, log_level, app_env):
        if self._initialized:
            return

        self.logger = logging.getLogger("microservices_logger")
        #
        self._initialized = True














    @classmethod
    def instance(cls, log_level=logging.INFO, app_dev="DEV"):
        """



        :param log_level:
        :param app_dev:
        :return:
        """
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls(log_level, app_dev)
        return cls._instance











    def log(self, level, message, extra_logger_data = {}):
        print(message)