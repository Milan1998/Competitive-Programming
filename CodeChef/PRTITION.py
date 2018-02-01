from random import randint as rn
import itertools
def bf(x,n):
    l = list(itertools.product([0, 1], repeat = n))
    ans = -1
    for p in l:
        s1,s2 = 0,0
        for i in range(len(p)):
            if i == x - 1:
                continue
            if p[i] == 1:
                s1 += i+1
            else:
                s2 += i+1
        if s1 == s2:
            ans = 1
            r = p
            break
    if ans == -1:
        return("impossible")
    else:
        s = ""
        for i in range(n):
            if i == x - 1:
                s += '2'
                continue
            s += str(r[i])
        return(s)
def f(A,B):
    s1 = sum(A)
    s2 = sum(B)
    if((s1 - s2)%2 != 0):
        return 0
    return (s1 - s2)//2
def g(A,B):
    t = f(A,B)
    if t == 0:
        return -2,-2
    i, j = 0, 0
    while i < len(A) and j < len(B):
        diff = A[i] - B[j]
        if diff == t:
            return (A[i], B[j])
        elif diff < t:
            i += 1
        else:
            j += 1
for _ in range(int(input())):
    x, n = [int(i) for i in input().split(" ")]
    if 1 == 1:
        if 1 == 1:  # :) lolololololololololol 
            #print(x,n)
            if n < 5:  
                print(bf(x,n))
                continue
            if ((n*(n+1))//2 - x) % 2 != 0:
                print("impossible")
            else:
                l,m = [],[]
                s1,s2 = 0,0
                pre = 0
                #print(c)
                for p in range(n,0,-1):
                    if p == x:
                        continue
                    if s1 > s2:
                        m.append(p)
                        s2 += p
                    else:
                        l.append(p)
                        s1 += p
                """print(sum(l),l)
                print(sum(m),m)"""
                z,y = g(l,m)
                #print(z,y)
                if z == -2:
                    s = ['2']*n
                    for i in l:
                        s[i-1] = '0'
                    for i in m:
                        s[i-1] = '1'
                    print(''.join(s))
                    continue
                for i in range(len(l)):
                    if l[i] == z:
                        l[i] = y
                        break
                for i in range(len(m)):
                    if m[i] == y:
                        m[i] = z
                        break
                """print(sum(l),l)
                print(sum(m),m)"""
                s = ['2']*n
                for i in l:
                    s[i-1] = '0'
                for i in m:
                    s[i-1] = '1'
                print(''.join(s))
