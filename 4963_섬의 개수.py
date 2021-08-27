from sys import stdin
from collections import deque
a,b=map(int,stdin.readline().split())
dx=[-1,0,1,-1,1,-1,0,1]
dy=[-1,-1,-1,0,0,1,1,1]
while a!=0 and b!=0:
    dq=deque([])
    l=[]
    count=0
    for i in range(b):
        l.append(list(map(int,stdin.readline().split())))
        check=[[0]*a for _ in range(b)]
    for i in range(b):
        for j in range(a):
            if check[i][j]==0 and l[i][j]==1:
                dq.append([i,j])
                check[i][j]=1
                count+=1
                while dq:
                    dqi,dqj=dq.popleft()
                    for k in range(8):
                        if a>dqj+dx[k]>=0 and b>dqi+dy[k]>=0:
                            if check[dqi+dy[k]][dqj+dx[k]]==0 and l[dqi+dy[k]][dqj+dx[k]]==1:
                                dq.append([dqi+dy[k],dqj+dx[k]])
                                check[dqi+dy[k]][dqj+dx[k]]=1
    print(count)
    a, b = map(int, stdin.readline().split())