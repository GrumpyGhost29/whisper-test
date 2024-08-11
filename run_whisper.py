import whisper
import os

print("Starting run!")

storagedir = 'storage'
indirpath = storagedir + '/inputs/'
outdirpath = storagedir + '/outputs/'
modeldirpath = storagedir + '/models'
infiles = os.listdir(indirpath)

# Add check here to see if the model exists, if so say downloading model
# If not say loading model instead

print(f"Downloading model to \"{modeldirpath}\" (this may take a while)...")
model = whisper.load_model("large", download_root="/app/storage/models")
print("Model loaded!")

print("Loading files...")
print(infiles)
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
