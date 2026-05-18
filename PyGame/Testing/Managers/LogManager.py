import logging

class LogManager:

    @staticmethod
    def Initialize():
        level = logging.DEBUG
        output: str = "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s"
        datefmt: str = '%Y-%m-%d %H:%M:%S'
        logging.basicConfig(level=level, format=output, datefmt=datefmt)

    @staticmethod
    def Write(msg: str):
        logging.info(msg, stacklevel=2)
