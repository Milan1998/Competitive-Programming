def binpow(a, b):
    res = 1
    cur = a
    while b > 0:
        if b & 1:
            res *= cur
        cur *= cur
        b >>= 1
    return res
for _ in range(int(raw_input())):
    a,n = [int(i) for i in raw_input().split(" ")]
    a = pow(a,n,9)
    if a == 0:
        print(9)
    else:
        print(a)
