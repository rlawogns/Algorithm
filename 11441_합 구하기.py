import sys
n = int(input())
l=list(map(int,sys.stdin.readline().split()))
Sum=[0]
for i in range(n):
   Sum.append(Sum[i]+l[i])
for i in range(int(input())):
   s,e=map(int,sys.stdin.readline().split())
   print(Sum[e]-Sum[s-1])