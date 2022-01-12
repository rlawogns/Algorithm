from collections import Counter
import sys
n=int(input())
l=[int(sys.stdin.readline()[:-1]) for _ in range(n)]
l.sort()
print(round(sum(l)/n))
print(l[n//2])
l2=Counter(l)
if n==1:
    print(l[0])
    print(0)
elif l2.most_common(2)[0][1] == l2.most_common(2)[1][1]:
    print(l2.most_common(len(l2))[1][0])
    print(l[-1] - l[0])
else:
    print(l2.most_common(1)[0][0])
    print(l[-1] - l[0])