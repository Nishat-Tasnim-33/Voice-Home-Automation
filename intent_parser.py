"""Rule-based intent parser: extracts (action, device, room) from a
transcribed voice command using keyword matching."""

ACTIONS = {
    "turn on": "on", "switch on": "on", "on": "on",
    "turn off": "off", "switch off": "off", "off": "off",
    "lock": "lock", "unlock": "unlock",
}
DEVICES = ["light", "fan", "lock", "door"]
ROOMS = ["living room", "bedroom", "kitchen", "front door"]


def parse_intent(text):
    text = text.lower()

    if "status" in text:
        return ("status", None, None)

    action = None
    for phrase, act in sorted(ACTIONS.items(), key=lambda kv: -len(kv[0])):
        if phrase in text:
            action = act
            break
    if action is None:
        return None

    device = "light" if "door" not in text and "lock" not in text else "lock"
    for d in DEVICES:
        if d in text:
            device = "lock" if d in ("lock", "door") else d
            break

    room = "front door" if "door" in text else None
    if room is None:
        for r in ROOMS:
            if r in text:
                room = r
                break
    if room is None:
        room = "living room"  # default

    return (action, device, room)
