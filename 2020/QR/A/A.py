import sys

def Solve(N, matrix):
    trace = 0
    row = 0
    col = 0
    for r in range(N):
        trace += matrix[r][r]
        checkList = [0 for x in range(N + 1)]
        for c in range(N):
            if checkList[matrix[r][c]] == 0:
                checkList[matrix[r][c]] = 1
            else:
                row += 1
                break
        
        checkList = [0 for x in range(N + 1)]
        for c in range(N):
            if checkList[matrix[c][r]] == 0:
                checkList[matrix[c][r]] = 1
            else:
                col += 1
                break

    return "%d %d %d" % (trace, row, col)

rl = lambda: sys.stdin.readline()

T = int(rl())
for t in range(T):
    N = int(rl())
    matrix = []
    for n in range(N):
        row = [int(x) for x in rl().split()]
        matrix.append(row)

    print("Case #%d: %s" % (t + 1, Solve(N, matrix)))
