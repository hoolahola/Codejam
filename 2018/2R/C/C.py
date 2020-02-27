
def solve(N, cells):
    vDicts = {}
    for r in range(N):
        for c in range(N):
            value = cells[r][c]
            if value in vDicts:
                vDicts[value].append((r, c))
            else:
                vDicts[value] = [(r, c)]
    cnt = 0
    for v in vDicts.keys():
        l = vDicts[v]
        rD = {}
        cD = {}
        rows = set()
        cols = set()
        for r, c in l:
            if r in rD:
                rD[r] += 1
            else:
                rD[r] = 1

            if c in cD:
                cD[c] += 1
            else:
                cD[c] = 1


    return cnt

T = int(input())
for i in range(T):
    N = int(input())
    cells = []
    for j in range(N):
        cells.append([int(x) for x in input().split()])
    output = solve(N, cells)
    print("Case #%d: %s" % ((i + 1), output))
