from sys import stdin
from collections import deque
n,m = map(int,stdin.readline().split())
nl=list(map(int,stdin.readline().split()))
l=[i for i in range(1,n+1)]
i=0
result=0
dq=deque(l)
while i<m:
    lc=0
    rc=0
    ldq=deque(l)
    rdq=deque(l)
    if ldq[0]==nl[i]:
        ldq.popleft()
        l=list(ldq)
        i+=1
        continue
    while True:
        if ldq[0]!=nl[i]:
            ldq.rotate(-1)
            lc+=1
        else:
            ldq.popleft()
            break
    while True:
        if rdq[0]!=nl[i]:
            rdq.rotate(1)
            rc+=1
        else:
            rdq.popleft()
            break
    if lc>rc:
        result+=rc
    else:
        result+=lc
    l=list(ldq)
    i+=1
print(result)