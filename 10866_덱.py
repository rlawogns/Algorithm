import collections
import sys
n=int(input())
l=collections.deque([])
for i in range(n):
    a=sys.stdin.readline()[:-1]
    if a.startswith("push_front"):
        b=a.split()[1]
        l.appendleft(b)
    elif a.startswith("push_back"):
        b = a.split()[1]
        l.append(b)
    elif a=="pop_front":
        if len(l)==0:
            print("-1")
        else:
            print(l.popleft())
    elif a=="pop_back":
        if len(l)==0:
            print(-1)
        else:
            print(l.pop())
    elif a=="size":
        print(len(l))
    elif a=="empty":
        if len(l)==0:
            print(1)
        else:
            print(0)
    elif a=="front":
        if len(l)==0:
            print(-1)
        else:
            print(l[0])
    elif a=="back":
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])