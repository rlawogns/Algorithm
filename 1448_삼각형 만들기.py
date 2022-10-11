from sys import stdin
n=int(input())
l=[int(stdin.readline().rstrip()) for _ in range(n)]
l.sort(reverse=True)
for i in range(0,n-2):
    if l[i]<l[i+1]+l[i+2]:
        print(sum(l[i:i+3]))
        exit()
print(-1)