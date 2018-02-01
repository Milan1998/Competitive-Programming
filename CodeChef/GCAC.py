for __ in range(int(input())):
    n,m=[int(i) for i in input().split(" ")]
    l,x,s,a1,a2=[],[],0,0,0
    a=[int(i) for i in input().split(" ")]
    for _ in range(m):
        temp=[int(i) for i in input().split(" ")]
        l.append([temp[0],s,temp[-1]])
        s+=1
    for i in range(n):
        x.append([int(a1) for a1 in input()])
    l.sort(reverse=True)
    comp=[0]*m
    for i in range(n):
        for j in range(m):
            if x[i][l[j][1]]==1 and l[j][0]>=a[i] and l[j][2]!=0:
                a1+=1
                a2+=l[j][0]
                l[j][2]-=1
                comp[j]=1
                break
    print(a1,a2,comp.count(0))
