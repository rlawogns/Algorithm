import sys
n=int(input())
l=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
l.sort(key=lambda x: (x[0],x[1]))
for i in l:
    print(i[0],i[1])