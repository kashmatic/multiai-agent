import subprocess
import threading
import time

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

from dotenv import load_dotenv

load_dotenv()

def run_backend():
  try:
    logger.info("Starting backend service")
    subprocess.run(["uvicorn", "app.backend.api:api", "--host", "127.0.0.1", "--port", "9999"], check=True)
  except Exception as e:
    logger.error(f"Error running backend {str(e)}")
    raise CustomException("Failed to start backend", e)

def run_frontend():
  try:
    logger.info("Starting frontend service")
    subprocess.run(["streamlit", "run", "app/frontend/ui.py"], check=True)
  except Exception as e:
    logger.error(f"Error running frontend {str(e)}")
    raise CustomException("Failed to start frontend", e)

if __name__ == '__main__':
  try:
    threading.Thread(target=run_backend).start()

    time.sleep(2)
    run_frontend()
  except Exception as e:
    logger.exception(f"Issue with threading {str(e)}")