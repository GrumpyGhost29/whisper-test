import os

indirpath = 'storage/inputs/'
infiles = os.listdir(indirpath)

for infile in infiles:
    if infile == '.gitkeep':
        continue
    outfile = 'storage/outputs/' + infile.split('.')[0] + '.txt'
    with open(outfile, 'w') as f:
        f.write('Hello World')