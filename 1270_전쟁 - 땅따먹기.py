from collections import Counter
from sys import stdin
n=int(input())
for _ in range(n):
    l=list(map(int,stdin.readline().split()))
    result = list(Counter(l[1:]).items())
    result.sort(key=lambda x : (-x[1]))
    if result[0][1]>(l[0]//2):
        print(result[0][0])
    else:
        print('SYJKGW')