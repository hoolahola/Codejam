import sys

def solve(R, C, H, V, cells):

    return 0

T = int(input())
for i in range(T):
    R, C, H, V = [int(x) for x in input().split()]
    cells = []
    for j in range(R):
        rows = [int(x) for x in input().split()]
        cells.append(rows)
    output = solve(R, C, H, V, cells)
    print("Case #%d: %s" % ((i + 1), output))
