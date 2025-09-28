import logging

logging.basicConfig(
    filename="disaster_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message: str):
    """Log disaster events to a file and console."""
    print(message)
    logging.info(message)
