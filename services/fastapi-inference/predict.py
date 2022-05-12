import logging
logger = logging.getLogger(__name__)


def predict(param1: float, param2: float):
    logger.info(f"Predict function called with {param1}, {param2}")
    return "I won't tell you."
