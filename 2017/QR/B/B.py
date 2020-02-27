import sys

def isTidy(N):
	maxNum = 0
	maxIdx = 0
	result = ''
	for i in range(len(N)):
		n = int(N[i])
		if n >= maxNum:
			maxNum = n
			maxIdx = i
		else:
			break

	return maxIdx == (len(N) - 1)

def tidy(N):
	maxNum = 0
	maxIdx = 0
	result = ''
	for i in xrange(len(N)):
		n = int(N[i])
		if n >= maxNum:
			maxNum = n
			maxIdx = i
		else:
			break

	if maxIdx == (len(N) - 1):
		return N
	
	for i in xrange(maxIdx):
		result += N[i]
	
	n = int(N[maxIdx]) - 1
	if n != 0 or maxIdx != 0:
		result += str(n)
	
	for i in xrange(maxIdx + 1, len(N)):
		result += '9'
	
	return result

def solve(N):
	
	while not isTidy(N):
		N = tidy(N)
		
	return N

f = open("B-large.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in range(T):
	N = rl()
	out = "Case #%d: %s\n" % (i + 1, solve(N))
	print out
	output.write(out)
