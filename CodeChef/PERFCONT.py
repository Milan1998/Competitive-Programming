for _ in range(int(input())):
    n,p=[int(i) for i in input().split(" ")]
    l=[int(i) for i in input().split(" ")]
    cc,ch=0,0
    for i in l:
        if i >= p//2:
            cc += 1
        if i <= p//10:
            ch +=1
    print("yes") if (cc == 1 and ch == 2) else print("no") 
