import sys
import math

def triangleArea(p1, p2, p3):
    area = p1[0] * p2[2] + p2[0] * p3[2] + p3[0] * p1[2] - p1[0] * p3[2] - p3[0] * p2[2] - p2[0] * p1[2]
    area = 0.5 * abs(area)
    return area

def polygonArea(points):
    area = 0
    if len(points) < 3:
        return area
    p1 = points[0]
    for i in range(1, len(points) - 1, 1):
        p2 = points[i]
        p3 = points[i + 1]
        area += triangleArea(p1, p2, p3)
    return area

def rotateX(p, radian):
    rotatedP = [0, 0, 0]
    rotatedP[0] = p[0]
    rotatedP[1] = p[1] * math.cos(radian) + p[2] * math.sin(radian)
    rotatedP[2] = p[1] * -math.sin(radian) + p[2] * math.cos(radian)
    return rotatedP

def rotateY(p, radian):
    rotatedP = [0, 0, 0]
    rotatedP[0] = p[0] * math.cos(radian) + p[2] * math.sin(radian)
    rotatedP[1] = p[1]
    rotatedP[2] = p[0] * -math.sin(radian) + p[2] * math.cos(radian)
    return rotatedP

def rotateZ(p, radian):
    rotatedP = [0, 0, 0]
    rotatedP[0] = p[0] * math.cos(radian) + p[1] * math.sin(radian)
    rotatedP[1] = -p[0] * math.sin(radian) + p[1] * math.cos(radian)
    rotatedP[2] = p[2]
    return rotatedP

def solve(A):
    forward = [0.5, 0, 0]
    up = [0, 0.5, 0]
    right = [0, 0, 0.5]

    forward = rotateY(forward, math.pi / 4)
    up = rotateY(up, math.pi / 4)
    right = rotateY(right, math.pi / 4)

    diff = 10
    minRange = 0
    maxRange = 0.9553161812
    radianX = 0
    vertex = [[0.5, 0.5, 0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5]]
    vertex = [rotateY(v, math.pi / 4) for v in vertex]
    minArea = polygonArea(vertex)
    vertexR = [rotateX(v, maxRange) for v in vertex]
    maxArea = polygonArea(vertexR)
    print(minArea)
    print(maxArea)
    while diff >= pow(10, -6):
        radianX = (minRange + maxRange) / 2
        vertexR = [rotateX(v, radianX) for v in vertex]
        area = polygonArea(vertexR)
        diff = abs(A - area)
        if A > area:
            minRange = radianX
        elif A < area:
            maxRange = radianX
        else:
            minRange = radianX
            maxRange = radianX
            break

    radianX = (minRange + minRange) / 2
    forward = rotateX(forward, radianX)
    up = rotateX(up, radianX)
    right = rotateX(right, radianX)

    return [forward, up, right]

T = int(input())
for i in range(T):
    A = float(input())
    outputs = solve(A)
    print("Case #%d:" % (i + 1))
    for output in outputs:
        print("%f %f %f" % (output[0], output[1], output[2]))
