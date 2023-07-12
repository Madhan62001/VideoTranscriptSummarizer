from preTrained import *
def makeTextFile(name, content):
    file = open(f"E:/Madhan/Project/Transcripts/{name}.txt","w",encoding="utf-8")
    file.write(f"{name} Transcript:\n")
    file.write(content)
    file.close()