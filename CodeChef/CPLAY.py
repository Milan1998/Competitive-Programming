import sys
for s in sys.stdin:
    if 1 == 1:
        l = []
        for i in s:
            if i == '1':
                l.append(1)
            else:
                l.append(0)
        s = [i for i in l]
        a,b,w,t = 0,0,0,0
        A = []
        B = []
        for i in range(10):
            if i%2 == 0:
                A.append(s[i])
            else:
                B.append(s[i])
        for i in range(5):
            a += A[i]
            if a > b:
                if a > b + 5 - i:
                    w = 'a'
                    t = 2 * i + 1
                    break
            else:
                if b > a + 4 - i:
                    w = 'b'
                    t = 2 * i + 1
                    break
            b += B[i]
            if b > a:
                if b > a + 4 - i:
                    w = 'b'
                    t = 2 * i + 2
                    break
            else:
                if a > b + 4 - i:
                    w = 'a'
                    t = 2 * i + 2
                    break
        if w != 0:
            if w == 'a':
                print("TEAM-A", t)
            else:
                print("TEAM-B", t)
              
        else:
           
            for i in range(10,19,2):
                if s[i] == 1:
                    a += 1
                if s[i + 1] == 1:
                    b += 1
                if a > b:
                    w = 'a'
                    t = i + 1
                    break
                elif b > a:
                    w = 'b'
                    t = i + 1
                    break
            if w == 0:
                print("TIE")
            else:
                if w == 'a':
                    print("TEAM-A", t + 1)
                else:
                    print("TEAM-B", t + 1)
