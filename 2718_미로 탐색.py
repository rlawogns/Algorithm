import sys
from collections import deque
n,m=map(int,input().split())
xl=[-1,0,1,0]
yl=[0,1,0,-1]
l=[sys.stdin.readline().rstrip() for i in range(n)]
check=[[0]*m for i in range(n)]
check[0][0]=1
min=0
dq=deque()
dq.append([0,0])
while(len(dq)>0):
    min+=1
    dqsize=len(dq)
    for i in range(dqsize):
        y,x=dq.popleft()
        if x==m-1 and y==n-1:
            print(min)
            dq.clear()
            break
        for i in range(4):
            xn = xl[i] + x
            yn = yl[i] + y
            if xn >= 0 and yn >= 0 and xn < m and yn < n:
                if l[yn][xn] == '1'and check[yn][xn]==0:
                    check[yn][xn]=1
                    dq.append([yn,xn])