import sys

def solve(N, K):
	i = 1
	a = N
	b = N
	aNum = 1
	bNum = 0
	while i < K:
		if a % 2 == 0:
			bNum = aNum + bNum * 2
		else:
			aNum = bNum + aNum * 2
		a = a / 2
		b = a - 1
		K -= i
		i *= 2

	if K <= aNum:
		N = a
	else:
		N = b

	return (N/2, (N-1)/2)

f = open("C-large.in")
#f = open("sample.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in range(T):
	line = rl().split()
	N = int(line[0])
	K = int(line[1])
	sol = solve(N, K)
	out = "Case #%d: %s %s\n" % (i + 1, sol[0], sol[1])
	print out
	output.write(out)
