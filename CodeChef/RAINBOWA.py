for _ in range(int(input())):
	n=int(input())
	l=[int(i) for i in input().split(" ")]
	x=["m"]
	m=["m",1,2,3,4,5,6,7,6,5,4,3,2,1]
	y=[l[i] for i in range(n-1,-1,-1)]
	for i in range(n):
		if x[-1]!=l[i]:
			x.append(l[i])
	if x==m and l==y:
		print("yes")
	else:
		print("no") 
