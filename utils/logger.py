import logging
import os

def setup_logger():
    """Configura el sistema de logging del proyecto"""
    logs_dir = "artifacts/logs"
    os.makedirs(logs_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(f"{logs_dir}/test_execution.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)