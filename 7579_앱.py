import sys
n,m=map(int,sys.stdin.readline().split())
am=list(map(int,sys.stdin.readline().split()))
ac=list(map(int,sys.stdin.readline().split()))
s=sum(ac)
l=[[0 for i in range(s+1)] for i in range(n)]
result=1000000001
for i in range(n):
   for j in range(s+1):
      if j>=ac[i]:
         l[i][j]=max(l[i-1][j-ac[i]]+am[i],l[i-1][j])
      else:
         l[i][j] = l[i-1][j]
      if l[i][j]>=m:
         result=min(result,j)
print(result)