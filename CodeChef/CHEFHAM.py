N = 100001
for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split(" ")]
    h = [0 for i in range(N)]
    for i in l:
        h[i] += 1
    x = [] #1s
    y = [] #2s
    """
    for i in range(N):
        if h[i] == 1:
            x.append(i)
        else:
            y.append(i)
    """
    if (2 not in h):
        if n == 1:
            print(0)
            print(l[0])
        else:    
            k = l[1:n]
            k.append(l[0])
            print(n)
            print(*k)
    elif (h.count(2) == 1 and n > 3):
        p = []
        q = []
        o = [d for d in l]
        h1 = [0 for i in range(N)]
        for i in range(n):
            if h1[l[i]] == 0:
                p.append(l[i])
                h1[l[i]] += 1
            else:
                q.append(l[i])
                l[i] = -1
        p1 = p[1:len(p)]
        p1.append(p[0])
        i1=0
        for i in range(n):
            if l[i]!=-1:
                l[i]=p1[i1]
                i1+=1
        for i in range(n):
            if q[0]!=o[i] and q[0]!=l[i]:
                l[l.index(-1)]=l[i]
                l[i]=q[0]
                break
        print(n)
        print(*l)
        
            
    else:
        if n == 2:
            print(0)
            print(*l)
        elif n == 3:
            if len(set(l)) == 1:
                print(0)
                print(*l)
            else:
                print(2)
                k = l[1:n]
                k.append(l[0])
                print(*k)
        else:
            p = []
            q = []
            h1 = [0 for i in range(N)]
            for i in range(n):
                if h1[l[i]] == 0:
                    p.append(l[i])
                    h1[l[i]] += 1
                else:
                    q.append(l[i])
                    l[i] = -1
            p1 = p[1:len(p)]
            p1.append(p[0])
            q1 = q[1:len(q)]
            q1.append(q[0])
            arr = []
            for i in range(n):
                if l[i] != -1:
                    arr.append(p1[0])
                    p1.pop(0)
                else:
                    arr.append(q1[0])
                    q1.pop(0)
            hu = 0
            for i in range(n):
                if l[i] != arr[i]:
                    hu += 1
            print(hu)
            print(*arr)
