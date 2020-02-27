import sys
import math

def solve(A):
    return ""

T = int(input())
for i in range(T):
    A = float(input())
    outputs = solve(A)
    print("Case #%d:" % (i + 1))

    for output in outputs:
        print("%f %f %f" % (output[0], output[1], output[2]))
