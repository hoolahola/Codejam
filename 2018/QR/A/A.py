import sys

def solve(D, P):
    totalD = 0
    currPower = 1
    totalHackCnt = 0

    shoots = []
    shootCnt = 0
    totalShootCnt = 0
    for c in P:
        if c == 'C':
            shoots.append([currPower, shootCnt])
            totalShootCnt += shootCnt
            shootCnt = 0
            currPower *= 2
        elif c == 'S':
            totalD += currPower
            shootCnt += 1
    if shootCnt > 0:
        shoots.append([currPower, shootCnt])
        totalShootCnt += shootCnt

    if totalShootCnt > D:
        return "IMPOSSIBLE"

    if len(shoots) <= 0:
        return 0

    remainD = totalD - D
    while remainD > 0:
        power, cnt = shoots[-1]
        hackCnt = min(cnt, int(remainD / power) + 1)
        remainD -= hackCnt * (power / 2)
        totalHackCnt += hackCnt
        shoots[-1][1] = cnt - hackCnt
        shoots[-2][1] += hackCnt
        if shoots[-1][1] <= 0:
            shoots.pop()

    return totalHackCnt

T = int(input())
for i in range(T):
    D, P = input().split()
    D = int(D)
    output = solve(D, P)
    print("Case #%d: %s" % ((i + 1), output))
