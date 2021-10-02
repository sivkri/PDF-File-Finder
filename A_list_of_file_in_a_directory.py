import glob

txtfiles = []
for file in glob.glob("*.pdf"):
    txtfiles.append(file)
    print(file)