for a0 in range(int(input())):
    n=int(input())
    l=list(map(int,input().split(' ')))
    print(l.index(min(l))+1)
