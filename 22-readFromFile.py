theList = {}

with open("22-nameslist.txt", "r") as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if str(line) not in theList.keys():
            theList[str(line)] = 1
        else:
            theList[str(line)] += 1
        line = open_file.readline()

print(theList)
