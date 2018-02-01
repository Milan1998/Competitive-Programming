from collections import defaultdict as dd
from math import sqrt as sq
def build(l):
    x = [l[0]]
    for i in range(1, len(l)):
        x.append(l[i] ^ x[-1])
    return x
def debug():
    print(blocks)
    print(p)
    print(mm)
    print(X)
    print(d)
n,q = [int(i) for i in raw_input().split(" ")]
l = [int(i) for i in raw_input().split(" ")]
if n > 1000:                     # WHY I DID THIS????
    nb = int(sq(n))
    zz = nb
    if sq(n) != int(sq(n)):
        nb += 1
    blocks = []
    for i in range(nb):
        blocks.append([])
    for i in range(n):
        blocks[i // zz].append(l[i])
    ll = len(blocks[0])
    #print(blocks)
    p = []
    for i in range(nb):
        x = 0
        for j in blocks[i]:
            x ^= j
        p.append(x)
    X = []
    for i in range(nb):
        k = [blocks[i][0]]
        for j in range(1, len(blocks[i])):
            k.append(blocks[i][j] ^ k[-1])
        X.append(k)
    d = []
    for i in X:
        d1 = dd(int)
        for j in i:
            d1[j] += 1
        d.append(d1.copy())
    #debug()
    for _ in range(q):
        Q = [int(i) for i in raw_input().split(" ")]
        if Q[0] == 2:
            ind = Q[1] - 1
            k = Q[2]
            blk = ind//ll
            blkind = ind - blk*ll + 1
            cur = k
            ans = 0
            for i in range(blk):
                ans += d[i][cur]
                cur ^= X[i][-1]
            xx = X[blk]
            for i in range(blkind):
                if xx[i] == cur:
                    ans += 1    
            print(ans)
            #debug()
        else:
            ind = Q[1] - 1
            x = Q[2]
            l[ind] = x
            blk = ind // ll
            blkind = ind - blk*ll
            blocks[blk][blkind] = x
            tmp = dd(int)
            t = 0
            for i in range(len(blocks[blk])):
                t ^= blocks[blk][i]
                X[blk][i] = t
                tmp[t] += 1
            d[blk] = tmp.copy()
else:
    for _ in range(q):
        t,x,k = [int(o) for o in raw_input().split(" ")]
        if t == 1:
            l[x - 1] = k
        else:
            ans = 0
            c = 0
            for i in range(1, x + 1):
                c ^= l[i - 1]
                if c == k:
                    ans += 1
            print(ans)
