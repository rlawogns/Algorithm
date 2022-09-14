from sys import stdin
from collections import deque
n,m=map(int,stdin.readline().split())
visit=[1,1]+[0 for _ in range(99)]
dq=deque([1])
dict={}
for _ in range(n):
    a,b=map(int,stdin.readline().split())
    dict[a]=b
for _ in range(m):
    a,b=map(int,stdin.readline().split())
    dict[a] = b
count=0
while True:
    count+=1
    tempdq=deque([])
    while len(dq)>0:
        temp=dq.popleft()
        for i in range(temp+1,temp+7):
            if i==100:
                print(count)
                exit()
            if i in dict:
                if visit[dict[i]]==0:
                    visit[dict[i]]=1
                    tempdq.append(dict[i])
            else:
                if visit[i]==0:
                    visit[i]=1
                    tempdq.append(i)
    dq=tempdq