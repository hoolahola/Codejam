import sys

def solveLarge(N, R, O, Y, G, B, V):
	stallR = ""
	stallY = ""
	stallB = ""

	if G > 0:
		if R < G:
			return "IMPOSSIBLE"
		R -= G
		N -= G * 2
		stallR = "GR" * G

	if V > 0:
		if Y < V:
			return "IMPOSSIBLE"
		Y -= V
		N -= V * 2
		stallY = "VY" * V

	if O > 0:
		if B < O:
			return "IMPOSSIBLE"
		B -= O
		N -= O * 2
		stallB = "OB" * O

	stall = ""
	colors = ['R', 'Y', 'B']
	nums = [R, Y, B]
	lastIndex = -1
	firstIndex = -1

	possible = True
	for i in xrange(N):
		index = -1
		m = -1
		for j in xrange(len(nums)):
			num = nums[j]
			if num > 0:
				if num == m and j != lastIndex:
					if j == firstIndex:
						index = j
				elif num > m and j != lastIndex:
					index = j
					m = num

		if m == -1:
			possible = False
			break

		if firstIndex == -1:
			firstIndex = index

		nums[index] = nums[index] - 1
		stall += colors[index]
		lastIndex = index
		if colors[index] == 'R':
			stall += stallR
			stallR = ""
		elif colors[index] == 'Y':
			stall += stallY
			stallY = ""
		elif colors[index] == 'B':
			stall += stallB
			stallB = ""

	if stallR != "" and stallB == "" and stallY == "" and stall == "":
		stall = stallR
		stallR = ""
	elif stallR == "" and stallB != "" and stallY == "" and stall == "":
		stall = stallB
		stallB = ""
	elif stallR == "" and stallB == "" and stallY != "" and stall == "":
		stall = stallY
		stallY = ""
	
	if stallR != "" or stallB != "" or stallY != "":
		possible = False

	if stall[0] == stall[-1]:
		possible = False

	if possible:
		return stall
	else:
		return "IMPOSSIBLE"

def solve(N, R, O, Y, G, B, V):
	stall = ""
	colors = ['R', 'Y', 'B']
	nums = [R, Y, B]
	lastIndex = -1
	firstIndex = -1

	possible = True
	for i in xrange(N):
		index = -1
		m = -1
		for j in xrange(len(nums)):
			num = nums[j]
			if num > 0:
				if num == m and j != lastIndex:
					if j == firstIndex:
						index = j
				elif num > m and j != lastIndex:
					index = j
					m = num

		if m == -1:
			possible = False
			break

		if firstIndex == -1:
			firstIndex = index

		nums[index] = nums[index] - 1
		stall += colors[index]
		lastIndex = index

	if stall[0] == stall[-1]:
		possible = False

	if possible:
		return stall
	else:
		return "IMPOSSIBLE"

f = open("B-large-practice.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in xrange(T):
	l = rl().split()
	N = int(l[0])
	R = int(l[1])
	O = int(l[2])
	Y = int(l[3])
	G = int(l[4])
	B = int(l[5])
	V = int(l[6])

	out = "Case #%d: %s\n" % (i + 1, solveLarge(N, R, O, Y, G, B, V))
	print out
	output.write(out)
