import logging

from .parser import build_path, read_sensor_data
from .reporter import sensor_summary

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("main started")
    data = read_sensor_data(build_path())
    sensor_summary(data)


if __name__ == "__main__":
    main()