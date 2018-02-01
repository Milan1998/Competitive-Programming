n=int(input())
for i in range(n):
    l=[int(i) for i in input().split(" ")]
    x=len(l)
    x-=1
    for i in range(x+1):
        if l[i]==x:
            l.pop(i)
            break
    print(max(l))
