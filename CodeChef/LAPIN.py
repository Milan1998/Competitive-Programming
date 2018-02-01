def solve(s1,s2):
    return(sorted(s1)==sorted(s2))
 
q=int(input())
for i in range(q):
    s=list(input())
    
    n=len(s)
    s1=s[0:n//2]
    if n%2==0:
        s2=s[n//2::]
    else:
        s2=s[n//2+1::]
    if solve(s1,s2):
        print("YES")
    else:
        print("NO")
