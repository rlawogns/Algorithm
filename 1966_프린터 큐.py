import collections
T=int(input())
for i in range(T):
    n,m=map(int,input().split())
    dq=collections.deque(list(map(int,input().split())))
    c=1
    while len(dq)>0:
        if dq[0]==max(dq):
            if m==0:
                print(c)
                break
            dq.popleft()
            c+=1
        else:
            dq.rotate(-1)
        m-=1
        if m==-1:
            m=len(dq)-1