import sys

def Solve(N, P):
    result = ""

    for c in P:
        if c == 'S':
            result += 'E'
        else:
            result += 'S'

    return result

rl = lambda: sys.stdin.readline()

T = int(rl())
for t in range(T):
    N = int(rl())
    P = rl().strip()
    print("Case #%d: %s" % (t + 1, Solve(N, P)))
