
def solve(N, weights):
    maxW = [6 * x for x in weights]
    totalW = [[0] * N, [0] * N]
    totalW[1][0] = weights[0]
    totalAnt = [[0] * N, [0] * N]
    totalAnt[1][0] = 1
    for i in range(N):
        if i == 0:
            continue

        mW = maxW[i]
        maxAnt = -1
        pW = 0
        for j in range(i):
            for k in range(2):
                if totalAnt[k][j] >= maxAnt and totalW[k][j] <= mW:
                    maxAnt = totalAnt[k][j]
                    pW = totalW[k][j]
        totalAnt[1][i] = maxAnt + 1
        totalW[1][i] = pW + weights[i]

        mW = maxW[i]
        maxAnt = -1
        pW = 0
        for j in range(i):
            for k in range(2):
                if totalAnt[k][j] >= maxAnt:
                    maxAnt = totalAnt[k][j]
                    pW = totalW[k][j]
        totalAnt[0][i] = maxAnt
        totalW[0][i] = pW

    index = 0 if totalAnt[0][-1] >= totalAnt[1][-1] else 1
    return totalAnt[index][-1]

T = int(input())
for i in range(T):
    N = int(input())
    weights = [int(x) for x in input().split()]
    output = solve(N, weights)
    print("Case #%d: %s" % ((i + 1), output))
