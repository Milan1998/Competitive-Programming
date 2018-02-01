for i in range(int(input())):
    u,v=[int(j) for j in input().split(" ")]
    print(((u+v)*(u+v+1)//2)+ u + 1) 
