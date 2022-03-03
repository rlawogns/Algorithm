from sys import stdin
n,m=map(int,input().split())
l=[0]+list(map(int,stdin.readline().split()))
for i in range(1,len(l)):
    l[i]=l[i-1]+l[i]
for _ in range(m):
    i,j=map(int,stdin.readline().split())
    print(l[j]-l[i-1])