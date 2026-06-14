import logging

class LogManager:

    @staticmethod
    def Initialize():
        level = logging.DEBUG
        level = logging.INFO
        #level = logging.ERROR
        #output: str = "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s"
        output: str = "[%(asctime)s] [%(module)s] %(message)s"
        datefmt: str = '%Y-%m-%d %H:%M:%S'
        logging.basicConfig(level=level, format=output, datefmt=datefmt)

    @staticmethod
    def Debug(msg: str):
        logging.debug(msg, stacklevel=2)

    @staticmethod
    def Write(msg: str):
        logging.info(msg, stacklevel=2)

    @staticmethod
    def Error(msg: str):
        logging.error(msg, stacklevel=2)
