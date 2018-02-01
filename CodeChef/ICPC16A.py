for _ in range(int(input())):
    a,b,c,d=[int(i) for i in input().split(" ")]
    if a==c:
        if b>d:
            print("down")
        else:
            print("up")
    elif b==d:
        if a>c:
            print("left")
        else:
            print("right")
    else:
        print("sad") 
