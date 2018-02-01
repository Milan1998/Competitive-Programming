for __ in range(int(input())):
    n,d=[int(i) for i in input().split(" ")]
    l=[int(i) for i in input().split(" ")]
    s=sum(l)
    e=s/n
    if e!=int(e):
        print(-1)
    else:
        e=int(e)
        c=0
        for i in range(n-d):
            if l[i]>e:
                c+=abs(e-l[i])
                l[i+d]+=l[i]-e
                l[i]=e
            else:
                c+=abs(e-l[i])
                l[i+d]-=e-l[i]
                l[i]=e
        if set(l)=={e}:
            print(c)
        else:
            print(-1)
