from sys import stdin
n,t,p=map(int,input().split())
tt=False
if n==0:
    print(1)
else:
    l=list(map(int,stdin.readline().split()))
    l.sort(reverse = True)
    for i in range(len(l)):
        if t>l[i]:
            l=l[:i]+[t]+l[i:]
            tt=True
            break
    if tt==False and n<p:
        l+=[t]
    elif tt==False and n>=p:
        print(-1)
        exit()
    r=l.index(t)+1
    if r>p:
        print(-1)
    else:
        print(r)

