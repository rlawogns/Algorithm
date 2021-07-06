import sys
from collections import deque
l= deque()
for _ in range(int(input())):
    a=sys.stdin.readline()
    s=a.split()[0]
    if (s=="push"):
        l.append(a.split()[1])
    elif (s=="front"):
        if (len(l) == 0):
            print(-1)
        else:
            print(l[0])
    elif (s=="back"):
        if (len(l) == 0):
            print(-1)
        else:
            print(l[-1])
    elif (s=="pop"):
        if (len(l) == 0):
            print(-1)
        else:
            print(l.popleft())
    elif (s == "size"):
        print(len(l))
    elif (len(l) == 0):
        print(1)
    else:
        print(0)