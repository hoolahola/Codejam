import sys


def solve(D, N, Horses):
	maxTime = 0
	for horse in Horses:
		K = horse[0]
		S = horse[1]
		T = float(D - K) / float(S)
		if T > maxTime:
			maxTime = T
	
	return float(D) / maxTime
	
f = open("A-large.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in xrange(T):
	line = rl().split()
	D = int(line[0])
	N = int(line[1])
	Horses = []
	for j in xrange(N):
		line = rl().split()
		Horses.append((int(line[0]), int(line[1])))

	out = "Case #%d: %s\n" % (i + 1, solve(D, N, Horses))
	print out
	output.write(out)
