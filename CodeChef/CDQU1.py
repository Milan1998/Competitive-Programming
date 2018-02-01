def solve(n,m):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    s = 0
    for p in range(2, n):
        if prime[p]:
            s += p
    for p in range(2, m):
    	if prime[p]:
            s -= p
    print(s)
for _ in range(int(input())):
	a,b = [int(i) for i in input().split(" ")]
	solve(b,a) 
