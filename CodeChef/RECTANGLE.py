for _ in range(int(input())):
    m = [int(i) for i in input().split(" ")]
    l = list(set(m))
    if len(l) == 1:
        print("YES")
    elif len(l) == 2:
        if m.count(l[0]) == 2 and m.count(l[1]) == 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
