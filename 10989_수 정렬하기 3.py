from sys import stdin
k=int(input())
l=[0]*10001
l.sort()
for _ in range(k):
    l[int(stdin.readline()[:-1])]+=1
for i in range(1,10001):
    if l[i]!=0:
        for _ in range(l[i]):
            print(i)