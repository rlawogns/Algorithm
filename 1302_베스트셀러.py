from sys import stdin
from collections import Counter
n=int(input())
l=[stdin.readline().rstrip() for _ in range(n)]
l.sort()
c=Counter(l)
print(c.most_common()[0][0])