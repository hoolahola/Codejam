import sys

def solve(R, B, C, cashiers):
    perBit = B // R
    times = []
    usingBits = []
    total_bit = 0
    
    for cashier in cashiers:
        bits = min(perBit, cashiers[0])
        total_bit += bits
        time = bits * cashiers[1] + cashiers[2]
        usingBits.append(bits)
        times.append(time)

    remainBits = B - total_bit

    while (remainBits > 0):
        minIndex = -1
        minTime = -1
        maxTime = -1
        for i in range(C):
            if usingBits[i] < cashiers[i][0]:
                if minTime < 0 or times[i] < minTime:
                    minTime = times[i]
                    minIndex = i
            if times[i] > maxTime:
                maxTime = times[i]
        if minIndex < 0:
            break


    return "OK"

T = int(input())
for i in range(T):
    R, B, C = [int(x) for x in input().split()]
    cashiers = []
    for j in range(C):
        cashiers.append([int(x) for x in input().split()])
    output = solve(R, B, C, cashiers)
    print("Case #%d: %s" % ((i + 1), output))
