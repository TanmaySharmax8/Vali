import sounddevice as sd
import json
import queue
from vosk import Model, KaldiRecognizer


# =========================
# VALI WAKE WORD SETTINGS
# =========================

MODEL_PATH = "vosk-model-small-en-us-0.15"

MICROPHONE_DEVICE = 1
SAMPLE_RATE = 44100

WAKE_WORDS = [
    "hey vali",
    "hello vali",
    "okay vali",
    "ok vali",
    "hey valley"
]


# =========================
# LOAD VOSK MODEL
# =========================

print("Loading Vali wake-word system...")

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
# WAIT FOR WAKE WORD
# =========================

def wait_for_wake_word():

    # Restrict recognition toward Vali's wake phrases
    grammar = json.dumps([
        "hey vali",
        "hello vali",
        "okay vali",
        "ok vali",
        "hey valley",
        "[unk]"
    ])

    recognizer = KaldiRecognizer(
        model,
        SAMPLE_RATE,
        grammar
    )

    print()
    print("Vali: Waiting for wake word...")
    print("Say: Hey Vali")
    print()

    # Start microphone
    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        device=MICROPHONE_DEVICE,
        dtype="int16",
        channels=1,
        callback=audio_callback
    ):

        while True:

            # Get microphone audio
            data = audio_queue.get()

            # Process speech
            if recognizer.AcceptWaveform(data):

                result = json.loads(
                    recognizer.Result()
                )

                text = result.get(
                    "text",
                    ""
                ).strip().lower()

                # Show recognized speech
                if text:

                    print("Heard:", text)

                    # Check for wake word
                    for wake_word in WAKE_WORDS:

                        if wake_word in text:

                            print()
                            print("Vali: Wake word detected!")
                            print()

                            return True


# =========================
# TEST WAKE WORD SYSTEM
# =========================

if __name__ == "__main__":

    wait_for_wake_word()