import sounddevice as sd
import json
import queue
from vosk import Model, KaldiRecognizer


MODEL_PATH = "vosk-model-small-en-us-0.15"

# Load Vosk model
print("Loading Vosk model...")
model = Model(MODEL_PATH)

# Audio queue
audio_queue = queue.Queue()


def audio_callback(indata, frames, time, status):
    """Receive microphone audio."""
    if status:
        print(status)

    audio_queue.put(bytes(indata))


# Use our working microphone
device = 1
sample_rate = 44100

recognizer = KaldiRecognizer(model, sample_rate)

print()
print("Vali local speech recognition is ready.")
print("Speak something...")
print("Press Ctrl+C to stop.")
print()

with sd.RawInputStream(
    samplerate=sample_rate,
    blocksize=8000,
    device=device,
    dtype="int16",
    channels=1,
    callback=audio_callback
):

    while True:

        data = audio_queue.get()

        if recognizer.AcceptWaveform(data):

            result = json.loads(recognizer.Result())

            text = result.get("text", "").strip()

            if text:
                print("You:", text)