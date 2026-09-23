import pytest
from lorapackage import parser

PATH_POSITIVE_TEST = "C:\\Andre\\ProvisioningGrounds\\modules\\m3-real-program\\tests\\test_readings_positve.txt"
PATH_NEGATIVE_TEST = "C:\\Andre\\ProvisioningGrounds\\modules\\m3-real-program\\tests\\test_readings_negative.txt"
EXPECTED_READINGS = [{"timestamp": "2026-09-15T08:12:03",
                    "node": "NODE_04",
                    "temp": 21.4,
                    "batt": 3.80},
                     {
                        "timestamp": "2026-09-15T08:12:10",
                      "node": "NODE_02",
                      "temp": 19.8,
                      "batt": 3.76
                      }
                     ]

def test_read_sensor_data_positive_test():
    sensor_data = parser.read_sensor_data(PATH_POSITIVE_TEST)

    assert len(sensor_data) == 2

    assert sensor_data[0]["node"] == EXPECTED_READINGS[0]["node"]
    assert sensor_data[0]["temp"] == EXPECTED_READINGS[0]["temp"]
    assert sensor_data[0]["batt"] == EXPECTED_READINGS[0]["batt"]

    assert sensor_data[1]["node"] == EXPECTED_READINGS[1]["node"]
    assert sensor_data[1]["temp"] == EXPECTED_READINGS[1]["temp"]
    assert sensor_data[1]["batt"] == EXPECTED_READINGS[1]["batt"]

def test_read_sensor_data_negative_test():
    with pytest.raises(parser.MalformedLogLineError):
        parser.read_sensor_data(PATH_NEGATIVE_TEST)
