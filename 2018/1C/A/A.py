import sys
import math

def solve(N, L, words):
    letters = [set() for x in range(L)]
    for word in words:
        for x in range(L):
            letters[x].add(word[x])

    letters = [list(x) for x in letters]
    indexs = [0 for x in range(L)]
    result = '-'
    while True:
        newWord = ''
        for i in range(L):
            newWord += letters[i][indexs[i]]
        if newWord in words:
            indexs[-1] += 1
            for i in reversed(range(L)):
                if indexs[i] >= len(letters[i]):
                    if i == 0:
                        return '-'
                    indexs[i] = 0
                    indexs[i - 1] += 1
            continue
        else:
            result = newWord
            break

    return result

T = int(input())
for i in range(T):
    N, L = [int(x) for x in input().split()]
    words = []
    for j in range(N):
        words.append(input())
    output = solve(N, L, words)
    print("Case #%d: %s" % ((i + 1), output))
