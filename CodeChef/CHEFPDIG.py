for a0 in range(int(input())):
    n=input()
    l=[0]*10
    for i in n:
        l[int(i)]+=1
    for z in range(65,91):
        x=str(z)
        a=int(x[0])
        b=int(x[1])
        if a==b:
            if l[a]>=2:
                print(chr(z),end="")
        else:
            if l[a]>=1 and l[b]>=1:
                print(chr(z),end="")
    print("")
