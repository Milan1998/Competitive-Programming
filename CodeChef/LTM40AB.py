for _ in range(int(input())):
    a,b,c,d=[int(i) for i in input().split(" ")]
    x=0
    for i in range(a,b+1):
        if i<c:
            x+=d-c+1
        elif i>=c and i<=d:
            x+=d-i
    print(x)
