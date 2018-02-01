for _ in range(int(input())):
    n,q = [int(i) for i in input().split(" ")]
    l = [int(i) for i in input().split(" ")]
    x = [int(i) for i in input().split(" ")]
    
    p = 1
    for i in range(n):
        p *= l[i]
    for i in x:
        print(i//p, end = " ")
    print() 
