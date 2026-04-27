import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("This message goes to both the console and the file.")
logging.debug("This is the debug level.")
logging.warning("This is the warning level.")
logging.error("This is the error level.")
logging.critical("This is the critical level.")

logger = logging.getLogger(__name__)

def process_data():
    logger.info("Processing data in this specific module...")

process_data()

"""
    EXPECTED OUTPUT:
    2026-04-25 23:55:19,424 - INFO - This message goes to both the console and the file.
    2026-04-25 23:55:19,424 - DEBUG - This is the debug level.
    2026-04-25 23:55:19,424 - WARNING - This is the warning level.
    2026-04-25 23:55:19,424 - ERROR - This is the error level.
    2026-04-25 23:55:19,424 - CRITICAL - This is the critical level.
    2026-04-25 23:55:19,424 - INFO - Processing data in this specific module...
"""