from sys import stdin
t=int(input())
for _ in range(t):
    m,n,x,y=map(int,stdin.readline().split())
    result=x
    while result<=m*n:
        if (result-x)%m==0 and (result-y)%n==0:
            print(result)
            break
        result+=m
    if result<=m*n:
        continue
    else:
        print(-1)