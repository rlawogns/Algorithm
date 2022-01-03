import collections
n,k = map(int,input().split())
dl = collections.deque([i+1 for i in range(n)])
print("<",end='')
while(len(dl)>1):
    dl.rotate(-(k-1))
    print(dl.popleft(),end=', ')
print(dl.popleft(),end='')
print(">")