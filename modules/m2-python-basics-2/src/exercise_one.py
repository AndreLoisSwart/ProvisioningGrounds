from pathlib import Path

def build_path() -> Path:
    current_path = Path(__file__).resolve().parent.parent
    return current_path / "readings.txt" 

def average(numbers: list) -> float:
    return sum(numbers) / len(numbers)

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
            

def unique_nodes(sensor_data: list[dict]) -> set:
    node_ids = {item["node"] for item in sensor_data}
    return node_ids

def battery_average(sensor_data: list[dict]) -> float:
    battery_voltages = [voltage_record["batt"] for voltage_record in sensor_data]

    return average(battery_voltages)

def sensor_summary(sensor_data: list[dict]):
    print(f"Current number of readings: {len(sensor_data)}")
    print(f"Relevant nodes: {", ".join(sorted(unique_nodes(sensor_data)))}")
    print(f"Average battery voltage: {battery_average(sensor_data)}V")


def main():
    data = read_sensor_data(build_path())
    sensor_summary(data)

if __name__ == "__main__":
    main()