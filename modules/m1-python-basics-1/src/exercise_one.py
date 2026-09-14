tuple_of_amps = (0.3, 1.2,3.4,20.0)

IDLE = 0.4
RUNNING = 15


def check_current(current: float) -> str:
    if current <= IDLE:
        return "idle"
    elif current <= RUNNING:
        return "running"
    else:
        return "fault"

def convert_to_readable_status(state: str, current: float) -> str:
    return f"{current}A -> {state}"



def main():
    for amp in tuple_of_amps:
        print(convert_to_readable_status(check_current(amp), amp))

if __name__ == "__main__":
    main()