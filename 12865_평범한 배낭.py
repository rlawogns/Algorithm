import sys
n,k=map(int,sys.stdin.readline().split())
item={0:0}
for i in range(n):
   a,b=map(int,sys.stdin.readline().split())
   temp={}
   for w, v in item.items():
      if w+a <= k:
         temp[w+a] = max(v+b,item.get(w+a,0))
   item.update(temp)
print(max(item.values()))