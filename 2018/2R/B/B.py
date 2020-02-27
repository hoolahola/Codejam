import sys
import math

def solve(R, B):
    remainR = R
    remainB = B
    r = 0
    b = 0
    cnt = 0

    while True:
        if remainR > remainB:

            pass
        elif remainB > remainR:
            pass
        else:
            pass

    return cnt

T = int(input())
for i in range(T):
    R, B = [int(x) for x in input().split()]
    output = solve(R, B)
    print("Case #%d: %s" % ((i + 1), output))
