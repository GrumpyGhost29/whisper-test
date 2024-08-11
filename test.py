import whisper
import os

path = 'inputs/'
files = os.listdir(path)
model = whisper.load_model("large")

for file in files:
    result = model.transcribe(path + file, language='de')
    print(result["text"])
