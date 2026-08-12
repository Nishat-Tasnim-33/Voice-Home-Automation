# Voice-Controlled Home Automation Simulator

Recognizes spoken commands ("turn on the living room light") and
controls a *simulated* smart home — extends your BAIUST IoT & Basic
Home Automation workshop experience into a working voice-interface
demo, no physical hardware needed.

## How it works
1. `smart_home.py` — a simulated house: a dict of rooms, each with
   devices (light, fan, door) and on/off/locked states, printed as an
   ASCII status board after every command.
2. `intent_parser.py` — lightweight rule-based NLU: extracts
   `(action, device, room)` from a transcribed sentence using keyword
   matching (no heavy NLP dependency required).
3. `voice_control.py` — uses `speech_recognition` to capture your
   microphone audio, transcribes it with Google's free Web Speech API,
   parses intent, and applies it to the simulated house.
4. `text_mode.py` — a fallback text-input version of the same demo, in
   case you want to show it off without a live microphone.

## Run it
```bash
pip install -r requirements.txt
python voice_control.py     # microphone version
# or
python text_mode.py         # type commands instead
```

## Example commands
"turn on the bedroom light", "turn off the kitchen fan",
"lock the front door", "status"
