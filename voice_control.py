"""Microphone-driven voice control loop for the smart home simulator."""
import speech_recognition as sr

from smart_home import SmartHome
from intent_parser import parse_intent

def main():
    home = SmartHome()
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Voice-controlled smart home ready. Say a command, or 'quit' to exit.")
    print(home.status())

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("\nListening...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"Heard: '{text}'")
        except sr.UnknownValueError:
            print("Sorry, didn't catch that.")
            continue
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
            continue

        if "quit" in text.lower() or "exit" in text.lower():
            break

        intent = parse_intent(text)
        if intent is None:
            print("Command not understood.")
            continue

        action, device, room = intent
        if action == "status":
            print(home.status())
        else:
            print(home.apply(action, device, room))


if __name__ == "__main__":
    main()
