n1,m1 = map(int,input().split())
l1=[list(map(int,input().split())) for _ in range(n1)]
n2,m2 = map(int,input().split())
l2=[list(map(int,input().split())) for _ in range(n2)]
result=[[0]*m2 for _ in range(n1)]
for i in range(m1):
	for j in range(n1):
		for k in range(m2):
			result[j][k]+=l1[j][i]*l2[i][k]
for i in result:
	print(*i)