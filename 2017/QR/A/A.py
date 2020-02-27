import sys

def flip(S, index, K):
	newS = S[:index]
	for i in xrange(K):
		if (S[index + i] == '+'):
			newS += '-'
		else:
			newS += '+'
	newS += S[index + K:]
	return newS

def solve(case, S, K):
	s = set([])

	result = "IMPOSSIBLE"
	count = 0

	for i in xrange(len(S) - K):
		if (S[i] == '-'):
			S = flip(S, i, K)
			count = count + 1

	remainBlack = 0

	for i in xrange(len(S) - K, len(S)):
		if (S[i] == '-'):
			remainBlack += 1

	if remainBlack == 0:
		result = str(count)
	elif remainBlack == K:
		count += 1
		result = str(count)

	output = "Case #%d: %s\n" % (case, result)
	print output
	return output

f = open("A-large.in")
rl = lambda: f.readline()

output = open("output.txt", 'w')

T = int(rl())
for i in range(T):
	line = rl().split()
	S = line[0]
	K = int(line[1])
	out = solve(i + 1, S, K)
	output.write(out)

