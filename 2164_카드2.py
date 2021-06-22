import collections
l=collections.deque([_ for _ in range(1,int(input())+1)])
while len(l)!=1:
    l.popleft()
    l.append(l.popleft())
print(l[0])