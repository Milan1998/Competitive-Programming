from collections import defaultdict as dd
import math
M=10**9+7
for _ in range(int(input())):
    n,q=[int(i) for i in input().split()]
    a=[0 for i in range(n+1)]
    qlist=[]
    for i in range(q):
        xx=[int(i) for i in input().split()]
        qlist.append(xx)
    b=int(math.sqrt(q))
    f,c=[],[]
    for i in range(0,q,b):
        fi=dd(int)
        for j in range(i,i+b):
            if j<q:
                lk=dd(int)
                if qlist[j][0]==1:
                    fi[qlist[j][1]]+=1
                    lk[qlist[j][1]]+=1
                    if qlist[j][2]+1<=n:
                        fi[qlist[j][2]+1]-=1
                        lk[qlist[j][2]+1]-=1
                    f.append(lk)
                if qlist[j][0]==2:
                    pk=dd(int)
                    for ik in range(qlist[j][1]-1,qlist[j][2]):
                        for ppk in f[ik]:
                            pk[ppk]+=(f[ik][ppk])
                    for mk in pk:
                        fi[mk]+=(pk[mk])
                    f.append(pk)
        c.append(fi)
    for i in c:
        for j in i:
            a[j]+=(i[j])
    for i in range(1,n+1):
        a[i]+=(a[i-1]%M)
        a[i]=a[i]%M
    a[n-1]=a[n-1]%M
    for i in range(1, len(a)):
        print(a[i],end=" ")
