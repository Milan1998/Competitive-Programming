for _ in range(int(input())):
    n = int(input())
    l = []
    ll = []
    for a in range(n):
        p = [int(i) for i in input().split(" ")]
        p.sort(reverse = True)
        ll.append(p)
    for i in range(n-1,-1,-1):
        l.append(ll[i].copy())
    ans = l[0][0]
    cur = l[0][0]
    t = 0
    for i in range(1,n):
        ck = 0
        for j in range(n):
            if l[i][j] < cur:
                ans += l[i][j]
                cur = l[i][j]
                ck += 1
                break
        if ck == 0:
            t = -1
    if t == 0:
        print(ans)
    else:
        print(-1)
