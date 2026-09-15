def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def unique_nodes(sensor_data: list[dict]) -> set[str]:
    node_ids = {item["node"] for item in sensor_data}
    return node_ids

def battery_average(sensor_data: list[dict]) -> float:
    battery_voltages = [voltage_record["batt"] for voltage_record in sensor_data]

    return average(battery_voltages)

def sensor_summary(sensor_data: list[dict]):
    print(f"Current number of readings: {len(sensor_data)}")
    print(f"Relevant nodes: {", ".join(sorted(unique_nodes(sensor_data)))}")
    print(f"Average battery voltage: {battery_average(sensor_data)}V")