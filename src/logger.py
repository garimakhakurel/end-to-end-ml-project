#logging all information about any execution that happens

import logging
import os
from datetime import datetime

#naming convention for logfile
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#path for the log file
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
#append the files even if there already exists files in the folder
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#overriding the functionality of logging
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

