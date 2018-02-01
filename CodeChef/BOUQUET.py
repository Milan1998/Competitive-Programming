for _ in range(int(input())):
    x=[]
    a1=[int(i) for i in input().split(" ")]
    a2=[int(i) for i in input().split(" ")]
    a3=[int(i) for i in input().split(" ")]
    if sum(a1)%2==0:
        x.append(sum(a1)-1)
    else:
        x.append(sum(a1))
    if sum(a2)%2==0:
        x.append(sum(a2)-1)
    else:
        x.append(sum(a2))
    if sum(a3)%2==0:
        x.append(sum(a3)-1)
    else:
        x.append(sum(a3))
    for i in range(3):
        s=a1[i]+a2[i]+a3[i]
        if s%2==0:
            x.append(s-1)
        else:
            x.append(s)
    if max(x)==-1:
        print(0)
    else:
        print(max(x))
