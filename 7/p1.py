LIMIT_SIZE = 100000

def getSize(text: list, accum: int, line: int, folders: list):
    i = line
    files=[]
    while i < len(text):
        print(f'accum {accum}, i {i}, line {line}, text {text[i]}')
        if text[i] == "$ cd ..":
            if accum >= LIMIT_SIZE:
                files = []
                accum = 0
            else:
                folders.append(accum)
            return i, accum, files
        elif text[i].startswith("$ cd"):
            exitLine, folderSize, subFiles = getSize(text, 0, i + 1, folders)
            if line == 1:
                subFiles = []
            print(subFiles)
            for file in subFiles:
                accum += int(file)
            #accum += folderSize
            i = exitLine
        elif text[i].split(" ")[0].isnumeric():
            accum += int(text[i].split(" ")[0])
            files.append(text[i].split(" ")[0])
        i += 1
    if accum >= LIMIT_SIZE:
        accum = 0
        files = []
    else:
        folders.append(accum)
    return i, accum, files




with open('/Users/EN24HB/advent2022/7/input.txt', 'r') as f:
    text = f.read()
folders = []
exitLine , total , filesInside = getSize(text.splitlines(), 0, 1, folders)
totalFolders = 0

print(folders)
for folder in folders:
    totalFolders += folder

print(totalFolders)
