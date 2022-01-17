from sys import stdin
n=int(input())
l=[list(map(int,stdin.readline().split())) for _ in range(n)]
l.sort(key=lambda x : (x[1], x[0]))
for i in l:
    print(i[0],i[1])