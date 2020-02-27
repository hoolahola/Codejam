import sys
import math

def solve(N, P, shapes):
    totalNocut = 0
    cuts = []
    for shape in shapes:
        nocut = shape[0] * 2 + shape[1] * 2
        cutMin = min(shape[0], shape[1]) * 2
        cutMax = math.sqrt(shape[0] * shape[0] + shape[1] * shape[1]) * 2

        totalNocut += nocut
        cuts.append((cutMin, cutMax))

    remainP = P - totalNocut

    if remainP == 0:
        return P

    closestP = 0
    closest = -1
    oldCuts = [(0, 0)]
    for cut in cuts:
        for oldCut in oldCuts:
            newCut = (cut[0] + oldCut[0], cut[1] + oldCut[1])
            if newCut[0] <= remainP and remainP <= newCut[1]:
                return P
            if newCut[1] < remainP:
                if closest < 0 or (remainP - newCut[1]) < closest:
                    closest = remainP - newCut[1]
                    closestP = newCut[1]
        oldCuts += [(cut[0] + oldCut[0], cut[1] + oldCut[1]) for oldCut in oldCuts]
    del oldCuts
    return totalNocut + closestP

T = int(input())
for i in range(T):
    N, P = [int(x) for x in input().split()]
    shapes = []
    for j in range(N):
        wi, hi = [int(x) for x in input().split()]
        shapes.append((wi, hi))
    output = solve(N, P, shapes)
    print("Case #%d: %s" % ((i + 1), output))