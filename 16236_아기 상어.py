from sys import stdin
from collections import deque
n=int(input())
l=[list(map(int,stdin.readline().split())) for _ in range(n)]
size=2
sizeCount=0
result=0
dx=[-1,0,0,1]
dy=[0,-1,1,0]
for i in range(n):
    for j in range(n):
        if l[i][j]==9:
            start=[i,j]
            l[i][j]=0
tdq=deque([start])
dq=tdq
visit=[[False]*n for _ in range(n)]
visit[start[0]][start[1]]=True
rc=-1
while tdq:
    dq=tdq
    dq = deque(sorted(list(tdq), key=lambda x: [x[0], x[1]]))
    tdq=deque([])
    rc+=1
    while dq:
        cx,cy=dq.popleft()
        if l[cx][cy] < size and l[cx][cy] > 0:
            sizeCount += 1
            if sizeCount == size:
                sizeCount = 0
                size += 1
            l[cx][cy] = 0
            dq.clear()
            tdq.clear()
            tdq.append([cx, cy])
            visit = [[False] * n for _ in range(n)]
            visit[cx][cy] = True
            start = [cx, cy]
            result+=rc
            rc=-1
            break
        for i in range(4):
            tx=cx+dx[i]
            ty=cy+dy[i]
            if tx<0 or ty<0 or tx>=n or ty>=n or visit[tx][ty]==True:
                continue
            else:
                if l[tx][ty] <= size:
                    tdq.append([tx,ty])
                    visit[tx][ty] = True
print(result)