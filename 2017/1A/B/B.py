import sys

def find(kits, k):
	for i in xrange(len(kits)):
		kk = kits[i]
		if k[1] >= kk[0] and kk[1] >= k[0]:
			return i

	return -1

def solve(N, P, Recipe, Packs):
	kits = []
	for n in xrange(N):
		kits.append([])
		r = Recipe[n]
		for p in xrange(P):
			pack = Packs[n][p]
			k = (pack / r) - 1
			kMin = -1
			kMax = 0
			for i in xrange(4):
				if k > 0:
					rate = float(pack) / float(k * r)
					if 0.9 <= rate and rate <= 1.1:
						if kMin == -1:
							kMin = k
						kMax = k

				k += 1

			if kMax != 0:
				kits[n].append((kMin, kMax))
	
	kitNum = 0

	kits[0].sort(key=lambda x: x[1])
	
	while len(kits[0]) > 0:
		kit = kits[0].pop()
		indexs = [0]
		possible = True

		for i in xrange(1, N):
			otherKits = kits[i]
			index = find(otherKits, kit)
			if index == -1:
				possible = False
				break
			else:
				indexs.append(index)

		if possible:
			for i in xrange(1, N):
				del kits[i][indexs[i]]
			kitNum += 1

	return kitNum

f = open("B-small-practice.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in range(T):
	l = rl().split()
	N = int(l[0])
	P = int(l[1])
	Recipe = []
	for r in rl().split():
		Recipe.append(int(r))
	Packs = []
	for n in xrange(N):
		Packs.append([])
		for p in rl().split():
			Packs[n].append(int(p))

	out = "Case #%d: %s\n" % (i + 1, solve(N, P, Recipe, Packs))
	print out
	output.write(out)
