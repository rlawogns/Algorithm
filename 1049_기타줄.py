from sys import stdin
n,m=map(int,stdin.readline().split())
min6=1000
min1=1000
for _ in range(m):
    a,b=map(int,stdin.readline().split())
    if min6>a:
        min6=a
    if min1>b:
        min1=b
if min1*6>min6:
    if (n//6)*min6+(n%6)*min1>(n//6+1)*min6:
        result=(n//6+1)*min6
    else:
        result=(n//6)*min6+(n%6)*min1
else:
    result=min1*n
print(result)
