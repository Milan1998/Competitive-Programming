for _ in range(int(raw_input())):
    x,y,z,a,b,c = [int(i) for i in raw_input().split(" ")]
    inf = 1<<32
    dp = []
    for i in range(x + 1):
        tmp = []
        for j in range(y + 1):
            tmp.append([inf for k in range(z + 1)])
        dp.append(tmp)
    #print(*dp)
    bb = min(b, 2*a)
    cc = min(c, a+b, 3*a)
    dp[0][0][0] = 0
    dp[1][0][0] = a
    dp[0][1][0] = a
    dp[0][0][1] = a
    dp[1][1][0] = bb
    dp[0][1][1] = bb
    dp[1][0][1] = bb
    dp[1][1][1] = cc
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                dp[i][j][k] = min(dp[i-1][j][k]+a,dp[i][j-1][k]+a,dp[i][j][k-1]+a,dp[i-1][j-1][k]+b,dp[i-1][j][k-1]+b,dp[i][j-1][k-1]+b,dp[i-1][j-1][k-1]+c)
    print(dp[x][y][z])
