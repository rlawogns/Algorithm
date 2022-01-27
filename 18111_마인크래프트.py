from sys import stdin
n,m,b=map(int,stdin.readline().split())
l=[list(map(int,stdin.readline().split())) for _ in range(n)]
result=[]
Min=min(map(min,l))
Max=max(map(max,l))
for i in range(Min,Max+1):
    bb=b
    tt=0
    for j in l:
        for k in j:
            t=i-k
            if t>0:
                bb-=t
                tt+=t
            elif t<0:
                bb+=-t
                tt+=-t*2
    if bb<0:
        tt=1000000000
    result.append([tt,i])
result.sort(key=lambda x:(x[0],-x[1]))
print(result[0][0],result[0][1])