import os
from singleton_logger import (SingletonLogger)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


SingletonLogger.instance(LOG_LEVEL)



SingletonLogger.instance().info("begin main")
#my_logger.info("begin main")

#test01()
#test02()

SingletonLogger.instance().info("-end- main")
