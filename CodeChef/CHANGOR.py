for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split(" ")]
    z = 0
    for i in l:
        z |= i
    print(z)
