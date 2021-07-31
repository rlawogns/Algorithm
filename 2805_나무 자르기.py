import sys
n,m=map(int,input().split())
l=list(map(int,sys.stdin.readline().split()))
p=1
q=max(l)
while p<=q:
   a = (p+q) // 2
   s=0
   for i in l:
      if i>a:
         s+=i-a
   if s>=m:
      p=a+1
   elif s<m:
      q=a-1
print(q)