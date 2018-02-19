def tidy(n):
	for x in range(18):
		for i in range(len(n) - 1):
			if n[i] > n[i + 1]:
				n[i] = str(int(n[i]) - 1)
				for j in range(i + 1, len(n)):
					n[j] = '9'
	return n
c = 1
for _ in range(int(input())):
	n = input()
	n = list(n)
	t = tidy(n)
	s = "Case #" + str(c) + ":"
	c += 1
	print(s,int(''.join(t)))
