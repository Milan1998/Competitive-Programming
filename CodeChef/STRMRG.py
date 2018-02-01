for _ in range(int(raw_input())):
    n, m = [int(i) for i in raw_input().split(" ")]
    a = raw_input().strip()
    b = raw_input().strip()
    l = [a[0]]
    m = [b[0]]
    for i in range(1,len(a)):
        if a[i] != l[-1]:
            l.append(a[i])
    for i in range(1,len(b)):
        if b[i] != m[-1]:
            m.append(b[i])
    #print(l,m)
    a = len(l)
    b = len(m)    
    dp = [[0 for i in range(b+1)] for j in range(a+1)]
    #print(a,b)
    x = a + b
    for i in range(a+1):
        for  j  in range(b+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif l[i - 1] == m[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1 
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
    p = dp[a][b]
    print(x - p)
