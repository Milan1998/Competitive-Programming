for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split(" ")]
    cn1,c1,cz=0,0,0
    for i in l:
        if i==1:
            c1+=1
        if i==0:
            cz+=1
        if i==-1:
            cn1+=1
    if n-(c1+cz+cn1)>1:
        print("no")
    elif n-(c1+cz+cn1)==1 and cn1>0:
        print("no")
    elif cn1>1 and c1==0:
        print("no")
    else:
        print("yes") 
