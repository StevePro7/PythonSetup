import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logEx01.log")
    ]
)

logging.getLogger(__name__)
logging.info("Logging setup complete!")