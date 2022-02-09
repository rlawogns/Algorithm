from sys import stdin
from collections import deque
n=int(input())
m=int(input())
e=[[] for _ in range(n)]
check=[0 for _ in range(n)]
for _ in range(m):
    a,b=map(int,stdin.readline().split())
    e[a-1].append(b)
    e[b-1].append(a)
dq=deque([1])
check[0]=1
while len(dq)!=0:
    t=dq.popleft()
    for i in e[t-1]:
        if check[i-1]==0:
            dq.append(i)
            check[i-1]=1
print(sum(check)-1)