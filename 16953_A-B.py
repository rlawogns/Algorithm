"""import collections   deque사용 a를 연산
a,b=map(int,input().split())
dq=collections.deque([a])
count=0
while len(dq)!=0:
   temp=dq.copy()
   count += 1
   dq.clear()
   for i in temp:
      if i==b:
         print(count)
         exit(0)
      if i*2<=b:
         dq.append(i*2)
      if i*10+1<=b:
         dq.append(i*10+1)
print(-1)"""

a,b=map(int,input().split())  #b를 거꾸로 연산
count=1
while b>0 and a!=b:
   if b%10==1:
      count+=1
      b//=10
   elif b%2==0:
      count+=1
      b//=2
   else:
      break
if a==b:
   print(count)
else:
   print(-1)