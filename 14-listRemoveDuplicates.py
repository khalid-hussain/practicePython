# Do the extras
# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html


def removeDuplicates(aList: list):
    return list(set(aList))


a = [5, 10, 15, 10, 30, 20, 25, 5, 10, 15, 15, 30]

print(removeDuplicates(a))
