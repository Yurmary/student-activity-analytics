import logging
import os
from datetime import datetime

def setup_logging():
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    today_str = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(logs_dir, f"log_{today_str}.txt")

    logging.basicConfig(
        filename=log_file,
        filemode="w",
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO
    )
