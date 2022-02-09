from sys import stdin
from sys import setrecursionlimit
def dfs(sn):
    if check[sn-1]==1:
        return
    check[sn-1]=1
    for i in e[sn-1]:
        dfs(i)
setrecursionlimit(15000)
n,m=map(int,stdin.readline().split())
e=[[] for _ in range(n)]
check=[0 for _ in range(n)]
result=0
for _ in range(m):
    a,b=map(int,stdin.readline().split())
    e[a-1].append(b)
    e[b-1].append(a)
for i in e:
    i.sort()

for i in range(n):
    if check[i]==0:
        dfs(i)
        result+=1
print(result)