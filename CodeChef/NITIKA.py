for _ in range(int(input())):
    l=[i for i in input().split(" ")]
    x=len(l)
    for i in range(x-1):
        print(l[i][0].upper() + ".", end=" ")
    print(l[-1][0].upper()+l[-1][1::].lower())
