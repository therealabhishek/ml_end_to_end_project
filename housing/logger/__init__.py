import logging
from datetime import datetime
import os


# log directory name:
LOG_DIR = "housing_logs"

# current time stamp:
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# log file name:
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

# creating directory:
os.makedirs(LOG_DIR, exist_ok=True)

# joining filepath and filename:
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
level = logging.INFO
)
