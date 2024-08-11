import whisper
import os

storagedir = 'storage'
indirpath = storagedir + '/inputs/'
outdirpath = storagedir + '/outputs/'
infiles = os.listdir(indirpath)
model = whisper.load_model("large", download_root="/app/models")

for infile in infiles:
    if infile == '.gitkeep':
        continue
    print(f'------------------------------------- processing file: {infile} -------------------------------------')
    outfile = outdirpath + infile.split('.')[0] + '.txt'
    print(outfile)
    transcript = model.transcribe(indirpath + infile, language='de')
    rawtext = transcript['text']
    text = transcript['text'].replace('. ', '.\n')
    text = text.lstrip()
    with open(outfile, 'w') as f:
        f.write(text)

print("done")
