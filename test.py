import whisper
import os

indirpath = 'inpuuuuuuts/'
infiles = os.listdir(indirpath)
model = whisper.load_model("large")

outdirpath = 'outputs/'

for file in infiles:
    if file == '.gitkeep':
        continue
    print(f'processing file: {file} -------------------------------------')
    result = model.transcribe(indirpath + file, language='de')
    with open(outdirpath + file, 'w') as f:
        f.write(result["text"])
