import sys
import math

def calcTargetCell(bottomLeft, topRight, cells):
    targetR, targetC = bottomLeft
    maxCell = -1

    for r in range(bottomLeft[0] + 1, topRight[0], 1):
        for c in range(bottomLeft[1] + 1, topRight[1], 1):
            cellCnt = 9
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if cells[r + i][c + j] == 1:
                        cellCnt -= 1
            if cellCnt > maxCell:
                maxCell = cellCnt
                targetR = r
                targetC = c

    return targetR, targetC

def solve(A):
    width = math.ceil(math.sqrt(A))
    height = math.ceil(A / width)
    bottomLeft = (500 - height // 2, 500 - width // 2)
    topRight = (500 + math.ceil(height / 2) - 1, 500 + math.ceil(width / 2) - 1)
    cells = [[0] * 1000 for x in range(1000)]

    while True:
        targetCell = calcTargetCell(bottomLeft, topRight, cells)
        print("%d %d" % (targetCell[0], targetCell[1]) )
        sys.stdout.flush()

        r, c = input().split()
        r = int(r)
        c = int(c)

        if r == -1 and c == -1:
            print('error')
            break

        if r == 0 and c == 0:
            break

        cells[r][c] = 1
        if r > topRight[0]:
            topRight = (r, topRight[1])
        elif r < bottomLeft[0]:
            bottomLeft = (r, bottomLeft[1])
        if c > topRight[1]:
            topRight = (topRight[0], c)
        elif c < bottomLeft[1]:
            bottomLeft = (bottomLeft[0], c)

T = int(input())
for i in range(T):
    A = int(input())
    solve(A)
