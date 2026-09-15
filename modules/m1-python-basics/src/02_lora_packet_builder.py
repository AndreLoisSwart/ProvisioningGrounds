message_pairs = (
    ("Bravo_one", "Bravo two, kggggt... come   in.  over."),
    ("Bravo_two", " Bravo one,  read you LOUD and cleAr.. kgggtttt..   over."),
    ("Bravo_one", " tEstIng MessAge Budget, ThinkIng About whaT to SaY iS Hard!  "),
    ("Bravo_two", " Here iS AnotheR MeSSage To  you bravo one..  Test TesT. "),
    (
        "Bravo_one",
        " TeSt tEst TeST TeSt tEst TeST TeSt tEst TeST TeSt tEst TeST TeSt tEst TeST TeSt tEst TeST ",
    ),
)

PAYLOAD_BUDGET = 80


def format_callsign(callsign: str) -> str:
    return callsign.strip().upper()


def clean_message(message: str) -> str:
    return " ".join(message.split())


def build_payload(callsign: str, message: str) -> str:
    return f"{callsign}:{message}"


def main():
    for callsign, message in message_pairs:
        packet = build_payload(format_callsign(callsign), clean_message(message))
        under_budget = len(packet) <= PAYLOAD_BUDGET
        if under_budget:
            print(f"packet: {packet}, budget remaining: {PAYLOAD_BUDGET - len(packet)}")
        else:
            print(f"packet: {packet}, budget exceeded by {len(packet) - PAYLOAD_BUDGET}")


if __name__ == "__main__":
    main()
