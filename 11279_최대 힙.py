from sys import stdin
import heapq
n= int(input())
hq=[]
for _ in range(n):
    m=int(stdin.readline()[:-1])
    if m==0:
        if len(hq)==0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq,(-m,m))