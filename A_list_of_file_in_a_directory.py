import glob

txtfiles = [file for file in glob.glob("*.pdf")]
for file in txtfiles:
    print(file)
