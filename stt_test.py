from openai import OpenAI

client = OpenAI()

audio_file = open("input.wav", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-transcribe",
    file=audio_file
)

print("You said:")
print(transcription.text)