import sys

def getNum(index, oddList, evenList):
    listToUse = oddList if index % 2 == 0 else evenList

    return listToUse[int(index / 2)]

def solve(N, V):
    oddList = []
    evenList = []
    odd = True

    for n in V:
        if odd:
            oddList.append(n)
        else:
            evenList.append(n)
        odd = not odd

    oddList.sort()
    evenList.sort()

    for i in range(N - 1):
        n = getNum(i, oddList, evenList)
        m = getNum(i + 1, oddList, evenList)
        if n > m:
            return i

    return "OK"

T = int(input())
for i in range(T):
    N = int(input())
    V = [int(x) for x in input().split()]
    output = solve(N, V)
    print("Case #%d: %s" % ((i + 1), output))
