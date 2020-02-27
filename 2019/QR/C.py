import sys

def Solve(N, Values):
    alphabetSet = set()
    primeValues = []
    primeNums = [2]

    for i in range(3, N + 1):
        isPrime = True
        for primeNum in primeNums:
            if i % primeNum == 0:
                isPrime = False
                break
        if isPrime:
            primeNums.append(i)
    
    firstValue = Values[0]
    primeNum1 = 0
    primeNum2 = 0
    for i in primeNums:
        if firstValue % i == 0:
            primeNum1 = i
            primeNum2 = firstValue / primeNum1

            if primeNum2 in primeNums:
                alphabetSet.add(primeNum1)
                alphabetSet.add(primeNum2)
                break

    for i in range(1,len(Values)):
        value = Values[i]
        if value % primeNum1 == 0:
            primeValues.append(primeNum2)
            primeNum2 = value / primeNum1
            if i == len(Values) - 1:
                primeValues.append(primeNum1)
                primeValues.append(primeNum2)
        else:
            primeValues.append(primeNum1)
            primeNum1 = value / primeNum2
            if i == len(Values) - 1:
                primeValues.append(primeNum2)
                primeValues.append(primeNum1)

        alphabetSet.add(primeNum1)
        alphabetSet.add(primeNum2)

    alphabets = sorted(alphabetSet)

    result = ""
    for primeValue in primeValues:
        result += chr(ord('A') + alphabets.index(primeValue))

    return result

rl = lambda: sys.stdin.readline()

T = int(rl())
for t in range(T):
    N, L = [int(x) for x in rl().split()]
    Values = [int(x) for x in rl().split()]
    print("Case #%d: %s" % (t + 1, Solve(N, Values)))
