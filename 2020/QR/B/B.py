import sys

def Solve(S):
    answer = ""
    depth = 0
    for c in S:
        digit = int(c)
        if digit == depth:
            answer += c
        elif digit > depth:
            answer += "(" * (digit - depth) + c
            depth = digit
        else:
            answer += ")" * (depth - digit) + c
            depth = digit

    answer += ")" * depth

    return answer

rl = lambda: sys.stdin.readline()

T = int(rl())
for t in range(T):
    S = rl().strip()
    print("Case #%d: %s" % (t + 1, Solve(S)))
