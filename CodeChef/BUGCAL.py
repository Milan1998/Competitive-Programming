for _ in range(int(input())):
    a, b = [i for i in input().split(" ")]
    ans = ""
    if len(a) > len(b):
        b = (len(a) - len(b)) * "0" + b
    else:
        a = (len(b) - len(a)) * "0" + a
    for i in range(len(a)):
        ans += str((int(a[i]) + int(b[i])) % 10)
    if ans == "0" * len(a):
        print("0")
    else:
        print(int(ans))
