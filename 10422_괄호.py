#카탈란 수
import math
mod=1000000007
for i in range(int(input())):
   m=int(input())
   if m%2==1:
      print(0)
   else:
      print(math.factorial(m)//math.factorial(m//2+1)//math.factorial(m//2)%mod)

"""	dp?
l=[1]
mod=1000000007
for i in range(1,2501):
   s = 0
   for j in range(i):
      s += (l[j] * l[i - 1 - j]) % mod
   s%=mod
   l.append(s)
for i in range(int(input())):
   m=int(input())
   if m%2==1:
      print(0)
   else:
      print(l[m//2])
"""