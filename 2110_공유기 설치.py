import sys
n,m=map(int,input().split())
l=[int(sys.stdin.readline().split()) for _ in range(n)]
l.sort()
s=1
e=l[-1]-l[0]
result=0
while(s<=e):
   mid = (s + e) // 2
   c=1                  #공유기설치한 개수
   current=l[0]         #현재주소
   for i in range(1,len(l)):
      if l[i]>=current+mid:
         c+=1
         current=l[i]
      if c>m:
         break
   if c>=m:
      result=mid
      s=mid+1
   else:
      e=mid-1
print(result)