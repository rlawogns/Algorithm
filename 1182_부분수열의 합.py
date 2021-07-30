import sys
import itertools
n,s=map(int,input().split())
result=0
l=list(map(int, sys.stdin.readline().split()))
for i in range(1,n+1)
   for j in itertools.combinations(l,i)
      if s==sum(j)
         result+=1
print(result)