t=int(input())
for i in range(t):
    a=int(input())
    l=[int(o) for o in input().split(" ")]
    x=l.count(1)
    y=a-x
    if x%2==0:
        print(y)
    else:
        print(x)
