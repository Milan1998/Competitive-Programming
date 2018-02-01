for a0 in range(int(input())):
    n=int(input())
    l=[i for i in range(1,n+1)]
    for i in range(0,n-1,2):
        l[i],l[i+1]=l[i+1],l[i]
    if n%2==1:
        l[-1],l[-2]=l[-2],l[-1]
    for i in l:
        print(i,end=" ")
    print("")
