for _ in range(int(input())):
    a,b,n=[int(i) for i in input().split(" ")]
    
    if n%2!=0:
        c,d=max(a*2,b),min(a*2,b)
        print(c//d)
    else:
        c,d=max(a,b),min(a,b)
        print(c//d)
