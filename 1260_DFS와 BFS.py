from sys import stdin
from collections import deque
def dfs(sn):
    if check[sn-1]==1:
        return
    check[sn-1]=1
    print(sn, end=' ')
    for i in e[sn-1]:
        dfs(i)
        
n,m,startn=map(int,stdin.readline().split())
e=[[] for _ in range(n)]
check=[0 for _ in range(n)]
for _ in range(m):
    a,b=map(int,stdin.readline().split())
    e[a-1].append(b)
    e[b-1].append(a)
for i in e:
    i.sort()

dfs(startn)
print('')

dq=deque([startn])
check=[0 for _ in range(n)]
check[startn-1]=1
while len(dq)!=0:
    t=dq.popleft()
    print(t, end=' ')
    for i in e[t-1]:
        if check[i-1]==0:
            dq.append(i)
            check[i-1]=1