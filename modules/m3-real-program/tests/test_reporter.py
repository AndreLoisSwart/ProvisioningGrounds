from lorapackage import reporter

FLOAT_LIST = [1.2, 2.2, 4.2, 1.0, 9.6]
DATA_LIST = [{
    "node":"NODE_1",
    "batt": 1.0
},{
    "node":"NODE_1",
    "batt": 1.0
},{
    "node":"NODE_2",
    "batt": 2.0
},{
    "node":"NODE_3",
    "batt": 3.0
}]

def test_average():
    assert round(reporter.average(FLOAT_LIST), 2) == 3.64

def test_unique_nodes():
    assert len(reporter.unique_nodes(DATA_LIST)) == 3

def test_battery_average():
    assert reporter.battery_average(DATA_LIST) == 1.75