import sys

def Solve(N):
    n1 = ""
    n2 = ""
    r = 0

    for i in range(len(N)):
        d = int(N[i]) + r
        
        if d == 1 and i < len(N) - 1:
            if (N[i + 1]) != "9":
                n1 += "0"
                n2 += "0"
                r = 10
                continue

        r = 0

        if d == 0:
            n1 += "0"
            n2 += "0"
        elif d <= 4:
            n1 += str(d - 1)
            n2 += "1"
        elif d == 9:
            n1 += "3"
            n2 += "6"
        elif d <= 14:
            n1 += "5"
            n2 += str(d - 5)
        else:
            n1 += "9"
            n2 += str(d - 9)
        
    n1 = n1[1:] if n1[0] == '0' else n1
    n2 = n2[1:] if n2[0] == '0' else n2

    return n1 + " " + n2

rl = lambda: sys.stdin.readline()

T = int(rl())
for t in range(T):
    N = rl().strip()
    print("Case #%d: %s" % (t + 1, Solve(N)))
