from sys import stdin
n=int(input())
m=int(input())
l=[[9999999 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,stdin.readline().split())
    l[a-1][b-1]=min(l[a-1][b-1],c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            l[i][j]=min(l[i][j],l[i][k]+l[k][j])
for i in range(n):
    for j in range(n):
        if l[i][j]==9999999 or i==j:
            l[i][j]=0
for i in l:
    for j in i:
        print(j,end=' ')
    print('')