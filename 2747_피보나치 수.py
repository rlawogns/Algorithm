n=int(input())
l=[]
for i in range(n):
   if i<=1:
      l.append(1)
   else:
      l.append(l[i-2]+l[i-1])
print(l[n-1])