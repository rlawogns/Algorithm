from sys import stdin
from collections import deque
n,m=map(int,input().split())
check=[]
dq=deque()
date=0
for i in range(m):
    l=list(map(int, stdin.readline().split()))
    for j in range(n):
        if l[j]==1:
            dq.append([i,j])
    check.append(l)
x=[-1,1,0,0]
y=[0,0,-1,1]
def bfs():
    while len(dq)!=0:
        xy=dq.popleft()
        for i in range(4):
            if 0 <= xy[1] + x[i] < n and 0 <= xy[0] + y[i] < m:
                if check[xy[0] + y[i]][xy[1] + x[i]] == 0:
                    check[xy[0] + y[i]][xy[1] + x[i]] = check[xy[0]][xy[1]]+1
                    dq.append([xy[0]+y[i],xy[1]+x[i]])
bfs()
for i in check:
    if 0 in i:
        date=0
        break
    date=max(date,max(i))
date-=1
print(date)