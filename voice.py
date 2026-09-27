import pyttsx3
import sounddevice as sd
import json
import queue
from vosk import Model, KaldiRecognizer


# =========================
# VALI VOICE OUTPUT
# =========================

engine = pyttsx3.init()

voices = engine.getProperty("voices")

# Microsoft David
engine.setProperty("voice", voices[0].id)

# Speaking speed
engine.setProperty("rate", 175)

# Volume
engine.setProperty("volume", 1.0)


def speak(text):
    """Make Vali speak."""

    engine.say(text)
    engine.runAndWait()


# =========================
# VALI SPEECH RECOGNITION
# =========================

MODEL_PATH = "vosk-model-small-en-us-0.15"

MICROPHONE_DEVICE = 1

# Vosk works well with 16 kHz speech input
SAMPLE_RATE = 16000


# =========================
# LOAD MODEL
# =========================

print("Loading Vali speech recognition...")

model = Model(MODEL_PATH)

audio_queue = queue.Queue()


# =========================
# AUDIO CALLBACK
# =========================

def audio_callback(indata, frames, time, status):

    if status:
        print(status)

    audio_queue.put(bytes(indata))


# =========================
# LISTEN
# =========================

def listen():

    recognizer = KaldiRecognizer(
        model,
        SAMPLE_RATE
    )

    print("Vali: Listening...")

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=4000,
        device=MICROPHONE_DEVICE,
        dtype="int16",
        channels=1,
        callback=audio_callback
    ):

        while True:

            data = audio_queue.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(
                    recognizer.Result()
                )

                text = result.get(
                    "text",
                    ""
                ).strip()

                if text:
                    return text


# =========================
# VOICE TEST
# =========================

if __name__ == "__main__":

    speak(
        "Hello. I am Vali. "
        "My voice system is online."
    )

    text = listen()

    print("You said:", text)

    speak(f"You said {text}")