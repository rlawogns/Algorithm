from sys import stdin
from collections import deque
n=int(input())
treelist=[[] for _ in range(n+1)]
visit=[False for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,stdin.readline().split())
    treelist[a]=treelist[a]+[b]
    treelist[b] = treelist[b] + [a]
result=[0 for _ in range(n+1)]
dq=deque([1])
visit[1]=True
while len(dq)>0:
    temp=dq.popleft()
    for i in treelist[temp]:
        if visit[i]==False:
            dq.append(i)
            visit[i]=True
            result[i]=temp
print(*result[2:],sep='\n')