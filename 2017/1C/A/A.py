import sys
import math

def solve(N, K, cakes):
	sortedCakes = list(map(lambda x : (2 * math.pi * x[0] * x[1], x[0], x[1]), cakes))
	sortedCakes.sort(reverse=True)

	surface = 0.0
	choosenCakes = sortedCakes[0 : K]
	for cake in choosenCakes:
		surface += cake[0]
	
	maxR = max(choosenCakes, key=lambda x : x[1])[1]
	circleSurface = math.pi * maxR * maxR
	surface += circleSurface
	minSurface = min(choosenCakes, key=lambda x : x[0])[0]
	
	remainCakes = sortedCakes[K :]
	maxAdd = 0
	for cake in remainCakes:
		if cake[1] > maxR:
			add = math.pi * cake[1] * cake[1] - circleSurface
			add -= minSurface + cake[0]
			if add > maxAdd:
				maxAdd = add

	print choosenCakes
	print remainCakes
	print maxAdd
	surface += maxAdd

	return surface

f = open("A-small-attempt1.in")
#f = open("sample.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in xrange(T):
	splits = rl().split()
	N = int(splits[0])
	K = int(splits[1])
	cakes = []
	for n in xrange(N):
		splits = rl().split()
		R = int(splits[0])
		H = int(splits[1])
		cakes.append((R, H))

	out = "Case #%d: %f\n" % (i + 1, solve(N, K, cakes))
	print out
	output.write(out)
