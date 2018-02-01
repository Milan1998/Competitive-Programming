def get(a,b):
    a += b
    a = str(a)
    c,d = 0,0
    for i in range(len(a)):
        if int(a[i])%2 == 0:
            c += int(a[i])
        else:
            d += int(a[i])
    return(abs(c - d))
N = 1000001
dp = [0 for i in range(N)]
dp[1] = 2
for i in range(2,N):
    dp[i] = dp[i - 1] + get(i, i) + get(i, i - 1) - get(i - 1, 1)
dp2 = [0 for i in range(N)]
dp2[1] = 2
for i in range(2,N):
    dp2[i] = dp2[i - 1] + 2*dp[i] - get(i, i) 
for _ in range(input()):
    n = input()
    print(dp2[n])
