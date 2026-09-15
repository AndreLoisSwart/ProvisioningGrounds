from .parser import build_path, read_sensor_data
from .reporter import sensor_summary


def main():
    data = read_sensor_data(build_path())
    sensor_summary(data)

if __name__ == "__main__":
    main()