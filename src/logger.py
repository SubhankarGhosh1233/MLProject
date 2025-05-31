import logging
import os
from datetime import datetime

# Use 12-hour format with AM/PM
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%I_%M_%S_%p')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%m/%d/%Y %I:%M:%S %p"  # 12-hour format with AM/PM
)
