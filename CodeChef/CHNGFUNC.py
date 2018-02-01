a,b=[int(i) for i in input().split(" ")]
ans=0
for i in range(1,a+1):
    x=i*i+b
    ans+=abs(int(x**0.5)-i)
print(ans)
