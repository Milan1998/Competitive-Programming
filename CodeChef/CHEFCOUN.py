element_sz=[42953,42952,42952,42951,42951,42950,42950,42950,42949,42949]  
boundry=[10919,35000,20000,42049,37049,55050,47050,7050,37051,17051]
for _ in range(int(input())):
    n=int(input())
    a=element_sz[n-99991]
    b=boundry[n-99991]
    print(a+b,end=" ")
    for i in range(n-1):
        print(a,end=" ")
    print()
    #A=[a]*n
    #A[69]+=b
    #print(*A) 
