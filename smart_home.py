"""A simulated smart home: rooms with devices and simple on/off/lock
states, with a printable status board."""

class SmartHome:
    def __init__(self):
        self.rooms = {
            "living room": {"light": "off", "fan": "off"},
            "bedroom": {"light": "off", "fan": "off"},
            "kitchen": {"light": "off", "fan": "off"},
            "front door": {"lock": "locked"},
        }

    def apply(self, action, device, room):
        if room not in self.rooms or device not in self.rooms[room]:
            return f"Sorry, I don't know '{device}' in '{room}'."

        if device == "lock":
            self.rooms[room][device] = "locked" if action == "lock" else "unlocked"
        else:
            self.rooms[room][device] = "on" if action == "on" else "off"

        return f"{device.title()} in {room} is now {self.rooms[room][device]}."

    def status(self):
        lines = ["=== Smart Home Status ==="]
        for room, devices in self.rooms.items():
            dev_str = ", ".join(f"{d}: {s}" for d, s in devices.items())
            lines.append(f"  {room.title():<14} {dev_str}")
        return "\n".join(lines)
