import logging
import os
import sys
from datetime import datetime
try:
    from src.exception import CustomException
except ImportError:
    from exception import CustomException

LOG_FILE=f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

if __name__ == "__main__":
    logging.info("Logging has started")
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divison by zero") 
        raise CustomException(e, sys)