def firstAndLast(aList: list):
    if len(aList) > 0:
        return [aList[0], aList[-1]]
    return []


a = [5, 10, 15, 20, 25]

print(firstAndLast(a))
