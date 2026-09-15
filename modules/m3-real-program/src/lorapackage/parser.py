from pathlib import Path


def build_path() -> Path:
    current_path = Path(__file__).resolve().parent.parent.parent
    return current_path / "readings.txt" 

def read_sensor_data(path: str | Path) -> list[dict]:
    sensor_data = []
    path = Path(path)

    with open(path) as f:
        for line in f:
            new_line = line.split(",")
            record = {
                    "timestamp": new_line[0],
                    "node": new_line[1],
                    "temp":float(new_line[2].split("=")[1]),
                    "batt": float(new_line[3].split("=")[1])
                }
            sensor_data.append(record)
    return sensor_data
