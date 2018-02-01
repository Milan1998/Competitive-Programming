from math import ceil as cc
 
for _ in range(int(input())):
    a=input().split()
    p,b=int(a[0]),int(a[1])
    k=int(p/(2*b))
    k1=cc(p/(2*b))
    #print(int(p**2/(4*b)))
    #x=p-k*b
    #print(x*k)
    print(max(p*k-(k**2)*b,p*k1-(k1**2)*b))
