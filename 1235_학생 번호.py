from sys import stdin
n = int(input())
l=[stdin.readline().rstrip() for _ in range(n)]
i=len(l[0])-1
setl=['']*n
while i>=0:
    for j in range(n):
        setl[j]=l[j][i]+setl[j]
    if len(set(setl))==n:
        print(len(setl[0]))
        break
    i-=1