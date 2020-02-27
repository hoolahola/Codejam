import sys

def solve(N, K, cakes):
	sortedCakes = sorted(cakes, key=lambda x: x[0])

	print sortedCakes
	
	return "IMPOSSIBLE"

f = open("B-large-practice.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in xrange(T):
	splits = rl().splits()
	N = int(splits[0])
	K = int(splits[1])
	cakes = []
	for n in xrange(N):
		splits = rl().splits()
		R = int(splits[0])
		H = int(splits[1])
		cakes.append((R, H))

	out = "Case #%d: %s\n" % (i + 1, solve(N, K, cakes))
	print out
	output.write(out)
