def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]
    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
    return max_so_far
for _ in range(int(input())):
    n, k = [int(i) for i in input().split(" ")]
    l = [int(i) for i in input().split(" ")]
    m = l.copy()
    m.reverse()
    suff = [l[0]]
    for i in range(1, n):
        suff.append(l[i] + suff[-1])
    #print(*suff)
    pref = [m[0]]
    for i in range(1, n):
        pref.append(m[i] + pref[-1])
    #print(*pref)
    if k < 5:
        print(maxSubArraySum(l*k, n*k))
    else:
        s = sum(l)
        l = 3*l
        a = maxSubArraySum(l, 3*n)
        print(max(a, (k-2)*s + max(suff) + max(pref)))
