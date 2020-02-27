
import sys

def CalcCandidate(board, R, C, currRow, currCol):
    candidate = []
    for r in range(R):
        for c in range(C):
            if r == currRow:
                continue
            if c == currCol:
                continue
            if r - c == currRow - currCol:
                continue
            if r + c == currRow + currCol:
                continue
            if board[r][c] == 0:
                candidate.append((r, c))
    return candidate

def Solve(R, C):
    board = []
    paths = []
    candidate = []
    currIndex = 0
    for r in range(R):
        col = []
        for c in range(C):
            col.append(0)
            candidate.append([])
            paths.append((-1, -1))
        board.append(col)

    for r in range(R):
        for c in range(C):
            candidate[0].append((r, c))
    
    result = True
    while currIndex != R * C:
        if len(candidate[currIndex]) == 0:
            if currIndex == 0:
                result = False
                break
            else:
                currIndex -= 1
                p = paths[currIndex]
                board[p[0]][p[1]] = 0                
        else:
            p = candidate[currIndex].pop()
            paths[currIndex] = p
            board[p[0]][p[1]] = 1
            currIndex += 1
            if currIndex == R * C:
                break
            else:
                candidate[currIndex] = CalcCandidate(board, R, C, p[0], p[1])

    resultStr = ""
    if result:
        resultStr += "POSSIBLE"
        for p in paths:
            resultStr += "\n" + str(p[0] + 1) + " " + str(p[1] + 1)
    else:
        resultStr += "IMPOSSIBLE"
    return resultStr

rl = lambda: sys.stdin.readline()

T = int(rl())
for t in range(T):
    R, C = [int(x) for x in rl().split()]
    print("Case #%d: %s" % (t + 1, Solve(R, C)))
