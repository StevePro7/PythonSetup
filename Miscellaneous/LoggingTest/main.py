import logging
from module_a import function_a
from module_b import function_b

# Configure logging
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("stevepro")


def main():
    logger.info("Starting main function")
    function_b()
    function_b()
    logger.info("Finished main function")


if __name__ == "__main__":
    main()