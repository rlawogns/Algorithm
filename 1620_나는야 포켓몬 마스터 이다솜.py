import sys
a,b=input().split()
l=[sys.stdin.readline().strip() for _ in range(int(a))]
d={}
for i in range(int(a)):
    d[l[i]]=i+1
for i in range(int(b)):
    q=sys.stdin.readline().strip()
    if q.isdigit():
        print(l[int(q)-1])
    else:
        print(d.get(q))