for _ in range(int(input())):
    n,k=[int(i) for i in input().split(" ")]
    l=[int(i) for i in input().split(" ")]
    l.sort()
    h=(n+k)//2
    print(l[h])
