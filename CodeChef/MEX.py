for _ in range(int(input())):
    n,k=[int(i) for i in input().split(" ")]
    l=[int(i) for i in input().split(" ")]
    h=[0]*200001
    for i in l:
        h[i]=1
    for i in range(200001):
        if h[i]==0:
            if k>0:
                k-=1
            else:
                print(i)
                break
