import sys


def solve(R, C, Rows):
	Grid = []
	firstRow = -1
	
	for i in xrange(R):
		row = Rows[i]
		Grid.append([])
		for j in xrange(C):
			Grid[i].append(row[j])
			if row[j] != '?' and firstRow == -1:
				firstRow = i

	startIndex = 0
	wasQ = False
	for i in xrange(C):
		char = Grid[firstRow][i]
		if char == '?':
			if not wasQ:
				startIndex = i
				wasQ = True
		elif wasQ:
			for j in xrange(startIndex, i):
				Grid[firstRow][j] = char
			wasQ = False
	if wasQ:
		for i in xrange(startIndex, C):
			Grid[firstRow][i] = Grid[firstRow][startIndex - 1]

	for i in xrange(firstRow + 1, R):
		startIndex = 0
		wasQ = False
		for j in xrange(C):
			char = Grid[i][j]
			if char == '?':
				if not wasQ:
					startIndex = j
					wasQ = True
			elif wasQ:
				for k in xrange(startIndex, j):
					Grid[i][k] = char
				wasQ = False

		if wasQ:
			if (startIndex > 0):
				for j in xrange(startIndex, C):
					Grid[i][j] = Grid[i][startIndex - 1]
			else:
				for j in xrange(C):
					Grid[i][j] = Grid[i - 1][j]

	for i in xrange(firstRow - 1, -1, -1):
		startIndex = 0
		wasQ = False
		for j in xrange(C):
			char = Grid[i][j]
			if char == '?':
				if not wasQ:
					startIndex = j
					wasQ = True
			elif wasQ:
				for k in xrange(startIndex, j):
					Grid[i][k] = char
				wasQ = False

		if wasQ:
			if (startIndex > 0):
				for j in xrange(startIndex, C):
					Grid[i][j] = Grid[i][startIndex - 1]
			else:
				for j in xrange(C):
					Grid[i][j] = Grid[i+1][j]

	output = ""
	for r in xrange(R):
		for c in xrange(C):
			output += Grid[r][c]
		if r != R - 1:
			output += '\n'

	return output

f = open("A-large.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in xrange(T):
	line = rl().split()
	R = int(line[0])
	C = int(line[1])
	Rows = []
	for j in xrange(R):
		Rows.append(rl())

	out = "Case #%d:\n%s\n" % (i + 1, solve(R, C, Rows))
	print out
	output.write(out)
