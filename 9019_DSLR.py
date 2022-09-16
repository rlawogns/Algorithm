from sys import stdin
from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,stdin.readline().split())
    dq=deque()
    dq.append((n,""))
    visit=set()
    visit.add(n)
    while dq:
        ns,result=dq.popleft()
        if ns==m:
            print(result)
            break
        t=(2*ns)%10000
        if t not in visit:
            dq.append((t,result+"D"))
            visit.add(t)
        t=(ns-1)%10000
        if t not in visit:
            dq.append((t, result + "S"))
            visit.add(t)
        t = (ns%1000)*10 + ns//1000
        if t not in visit:
            dq.append((t, result + "L"))
            visit.add(t)
        t = (ns%10)*1000 + ns//10
        if t not in visit:
            dq.append((t, result + "R"))
            visit.add(t)
