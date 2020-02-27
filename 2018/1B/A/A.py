import sys
import math

def solve(N, L, respons):
    Q = 100 // N
    R = 100 % N
    rr = R / N
    remainNum = N - sum(respons)

    if R / N >= 0.5 or R == 0:
        result = 0
        for num in respons:
            result += round((100 * num) / N)
        result += round(100 / N) * remainNum
        return result

    nums = [[0.5 - ((x * 100) % N) / N, x] for x in respons]
    while remainNum > 0:
        nums.sort()
        skip = nums[-1][0] > 0
        if skip:
            for i in range(len(nums)):
                num = nums[i]
                if skip and num[0] <= 0:
                    continue
                count = min(math.ceil(num[0] / rr), remainNum)
                remainNum -= count
                num[1] += count
                num[0] = 0.5 - ((num[1] * 100) % N) / N
                break
        else:
            num = nums[0]
            remainNum -= 1
            num[1] += 1
            num[0] = 0.5 - ((num[1] * 100) % N) / N

    result = 0
    for num in nums:
        result += round(num[1] * 100 / N)

    return result

T = int(input())
for i in range(T):
    N, L = [int(x) for x in input().split()]
    respons = [int(x) for x in input().split()]
    output = solve(N, L, respons)
    print("Case #%d: %s" % ((i + 1), output))
