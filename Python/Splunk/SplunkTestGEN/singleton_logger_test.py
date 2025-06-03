from singleton_logger import (SingletonLogger)

def test_logger():
    SingletonLogger.instance('INFO')
    SingletonLogger.instance().info("hello")

    assert 1 == 1