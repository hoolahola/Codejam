import sys

rl = lambda: sys.stdin.readline()

def Solve1(N, M):
    G = 0
    for n in range(N):
        print("18 " * 18)
        sys.stdout.flush()
        results = [int(x) for x in rl().split()]
        if results[0] == -1:
            exit()
        G = sum(results)
    print(G)

def Solve2(N, M):
    G = 0
    d = 18
    remains = []
    for n in range(N):
        print(str(d) + " " * 18)
        sys.stdout.flush()
        results = [int(x) for x in rl().split()]
        #if results[0] == -1:
        #    exit()
        remains.append(sum(results) % d)
        d -= 1

    x = 18
    y = 17
    r = 0
    r1 = remains[0]
    r2 = remains[1]

    if (r2 >= r1):
        r = (r2 - r1) * y + r2
        x = x * y
    else:
        temp = r2 + 1
        r1 = r1 - temp
        r2 = y - 1
        r = (r2 - r1) * y + r2 + temp
        x = x * y

    for i in range(2, len(remains)):
        y = 18 - i
        r1 = r
        r2 = remains[i]

        if (r2 >= r1):
            r = (r2 - r1) * y + r2
            x = x * y
        else:
            temp = r2 + 1
            r1 = r1 - temp
            r2 = y - 1
            r = (r2 - r1) * y + r2 + temp
            x = x * y

    print(x + r)

def Solve(N, M):
    if N == 365:
        Solve1(N, M)
    else:
        Solve2(N, M)

T, N, M = [int(x) for x in rl().split()]

for t in range(T):
    Solve(N, M)