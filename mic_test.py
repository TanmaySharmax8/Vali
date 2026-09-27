import sounddevice as sd
import scipy.io.wavfile as wav

print("Recording for 5 seconds...")
print("Please speak normally.")

sample_rate = 44100
duration = 5

recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16",
    device=1
)

sd.wait()

wav.write("input.wav", sample_rate, recording)

print("Recording complete.")
print("Saved as input.wav")