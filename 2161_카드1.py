from collections import deque
n=int(input())
l=[i for i in range(1,n+1)]
dq=deque(l)
result=[]
while len(dq)!=1:
    result.append(dq.popleft())
    dq.rotate(-1)
result.append(dq.pop())
print(*result)
