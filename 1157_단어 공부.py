from sys import stdin
from collections import Counter
s=stdin.readline().rstrip()
c=Counter(s.upper())
c=list(c.items())
c.sort(key= lambda x: -x[1])
if len(c)==1:
    print(c[0][0])
else:
    if c[0][1]==c[1][1]:
        print("?")
    else:
        print(c[0][0])