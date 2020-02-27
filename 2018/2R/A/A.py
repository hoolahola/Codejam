import sys
import math

def solveR(C, row):


def solve(C, Bs):
    if Bs[0] == 0 or Bs[-1] == 0:
        return "IMPOSSIBLE"

    lastRow = Bs
    lamps = []
    lamps.append("." * C)
    while True:
        prevRow = [0] * C

        for i in range(C):
            n = lastRow[i]
            if n > 1:



    return rows

T = int(input())
for i in range(T):
    C = int(input())
    Bs = [int(x) for x in input().split()]
    output = solve(C, Bs)
    print("Case #%d: %s" % ((i + 1), output))
