import heapq

c = 1
for _ in range(int(input())):
	n, k = [int(i) for i in input().split(" ")]
	h = [[-(n - 1) - 1, 1, n]]
	for i in range(k):
		p = heapq.heappop(h)
		sz = -p[0]
		l = p[1]
		r = p[2]
		m = (r + l) // 2
		ls = -(-(m - l - 1) - 1)
		rs = -(-(r - (m + 1)) - 1)
		x = [-ls, l, m - 1]
		y = [-rs, m + 1, r]
		heapq.heappush(h, x)
		heapq.heappush(h, y)
	a1 = max(ls, rs)
	a2 = min(ls, rs)
	s = "Case #" + str(c) + ":"
	c += 1
	print(s,a1,a2)

