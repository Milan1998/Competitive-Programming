for  _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("Draw")
        continue
    l = []
    for i in range(n):
        l.append(input())
    s = list(set(l))
    x = len(s)
    if x == 1:
        print(s[0])
        continue
    if l.count(s[0]) > l.count(s[1]):
        print(s[0])
    elif l.count(s[0]) < l.count(s[1]):
        print(s[1])
    else:
        print("Draw")
