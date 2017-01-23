def isInList(aList: list, numberToSearch: int):
    if numberToSearch in aList:
        return True
    else:
        return False


def listBinarySearch(aList: list, numberToSearch: int):
    return True


if __name__ == "__main__":
    a = [1, 3, 5, 30, 42, 43, 500]
    b = [1, 3, 5, 30, 42, 43, 500, 96]
    intToSearch = 9
    print(isInList(a, intToSearch))
    # print("a:", len(a) / 2)
    # print("b:", len(b) / 2)
