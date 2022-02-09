from sys import stdin
a,b=map(int,input().split())
la=set(list(map(int,stdin.readline().split())))
lb=set(list(map(int,stdin.readline().split())))
print(len(la-lb)+len(lb-la))