import logging
from pathlib import Path


class MalformedLogLineError(ValueError):
    pass

logger = logging.getLogger(__name__)

def build_path() -> Path:
    logger.info("Building log path.")
    current_path = Path(__file__).resolve().parent.parent.parent
    return current_path / "readings.txt"


def read_sensor_data(path: str | Path) -> list[dict]:
    logger.info(f"Reading sensor data from {path}")
    sensor_data = []
    path = Path(path)
    try:
        with open(path) as f:
            for line in f:
                new_line = line.split(",")
                record = {
                    "timestamp": new_line[0],
                    "node": new_line[1],
                    "temp": float(new_line[2].split("=")[1]),
                    "batt": float(new_line[3].split("=")[1])
                }
                sensor_data.append(record)
        return sensor_data
    except ValueError as e:
        logger.error(e)
        raise MalformedLogLineError(str(e))