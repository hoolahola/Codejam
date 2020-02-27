import sys

def solve(N):
    P = [0] * N
    lollipops = [1] * N

    for i in range(N):
        inputs = [int(x) for x in input().split()]
        if len(inputs) <= 0:
            return -1
        D = inputs[0]
        flavors = inputs[1:]
        if D < 0:
            return -1
        minP = -1
        minFlavor = -1
        for flavor in flavors:
            P[flavor] += 1
            if (minP < 0 or P[flavor] < minP) and lollipops[flavor] == 1:
                minP = P[flavor]
                minFlavor = flavor
        print(minFlavor)
        if minFlavor >= 0:
            lollipops[minFlavor] = 0

    return 0

T = int(input())
for i in range(T):
    N = int(input())
    if solve(N) < 0:
        break
