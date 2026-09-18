import logging
import argparse

from .parser import build_path, read_sensor_data
from .reporter import sensor_summary


logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default=None,type=str, help="Provide a path to your file, or leave blank to use fallback.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Turn on debug logging")

    args = parser.parse_args()

    log_level= logging.DEBUG if args.verbose else logging.INFO

    logging.basicConfig(level=log_level)

    logger.info("This message always shows up.")
    logger.debug("This message ONLY shows up if you used -v or --verbose.")

    file_path = args.file or build_path()

    data = read_sensor_data(file_path)
    sensor_summary(data)


if __name__ == "__main__":
    main()