for _ in range(int(input())):
    a=list(input())
    b=list(input())
    x,y=set(a),set(b)
    winner='B'
    if x.issubset(y):
        winner='B'
    elif y.issubset(x):
        winner='A'
    else:
        for i in x:
            if a.count(i)>1 and (i not in b):
                winner='A'
                break
    print(winner) 
