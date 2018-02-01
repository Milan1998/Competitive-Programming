for _ in range(int(input())):
    n,d = [i for i in input().split(" ")]
    l = [0 for i in range(7)]
    dd = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
    x = dd.index(d)
    n = int(n)
    while(n>0):
        l[x] += 1
        x = (x + 1) % 7
        n -= 1
    print(*l) 
