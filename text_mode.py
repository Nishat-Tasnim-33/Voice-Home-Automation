"""Text-input fallback for the smart home demo -- same logic as
voice_control.py, no microphone needed."""
from smart_home import SmartHome
from intent_parser import parse_intent


def main():
    home = SmartHome()
    print("Smart home text-mode demo. Type a command, or 'quit' to exit.")
    print(home.status())

    while True:
        text = input("\n> ").strip()
        if text.lower() in ("quit", "exit"):
            break

        intent = parse_intent(text)
        if intent is None:
            print("Command not understood. Try: 'turn on the bedroom light'")
            continue

        action, device, room = intent
        if action == "status":
            print(home.status())
        else:
            print(home.apply(action, device, room))


if __name__ == "__main__":
    main()
