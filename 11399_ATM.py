import sys
n=input()
l=sorted(list(map(int,sys.stdin.readline().split())))
s=0
t=0
for i in l:
   t+=i
   s+=t
print(s)