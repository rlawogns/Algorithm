from collections import deque
n,k=map(int,input().split())
check=[0 for _ in range(100001)]
t=[999999 for _ in range(100001)]
dq=deque([n])
t[n]=0
while(len(dq)!=0):
    c=dq.popleft()
    check[c]=1
    if c+1<100001 and check[c+1]==0:
        t[c+1]=t[c]+1
        check[c+1]=1
        dq.append(c+1)
    if  0<=c-1 and c-1<100001 and check[c-1]==0:
        t[c-1]=t[c]+1
        check[c-1]=1
        dq.append(c-1)
    if  c*2<100001 and check[c*2]==0:
        t[c*2]=t[c]+1
        check[c*2]=1
        dq.append(c*2)
    if t[k]!=999999:
        print(t[k])
        break