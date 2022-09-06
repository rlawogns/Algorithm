from sys import stdin
from collections import deque
T=int(input())
for _ in range(T):
    lr=True
    s=stdin.readline().rstrip()
    n=int(input())
    if n==0:
        l=input()
        if 'D' in s:
            print('error')
        else:
            print([])
        continue
    else:
        l=list(map(int,stdin.readline()[1:-2].split(',')))
    dq=deque(l)
    b=False
    for i in s:
        if i=='R':
            lr = not lr
        else:
            if len(dq)==0:
                b=True
                break
            if lr:
                dq.popleft()
            else:
                dq.pop()
    if b:
        print('error')
    else:
        print("[", end='')
        if lr:
            print(*list(dq),end='',sep=',')
        else:
            dq.reverse()
            print(*list(dq), end='', sep=',')
        print("]")