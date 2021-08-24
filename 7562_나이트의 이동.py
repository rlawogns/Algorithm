def asd(dq):
   while dq:
      i=dq.popleft()
      if i[0] == p[0] and i[1] == p[1]:
         return result[i[0]][i[1]]
      for j in range(8):
         if l > i[0] + dx[j] >= 0 and l > i[1] + dy[j] >= 0 and result[i[0] + dx[j]][i[1] + dy[j]] == 0:
            dq.append((i[0] + dx[j], i[1] + dy[j]))
            result[i[0] + dx[j]][i[1] + dy[j]] = result[i[0]][i[1]] + 1
import collections
n=int(input())
dx=[-2,-1,-2,-1,2,1,2,1]
dy=[-1,-2,1,2,1,2,-1,-2]
for i in range(n):
   l=int(input())
   result = [[0] * l for _ in range(l)]
   t = tuple(map(int, input().split()))
   p = tuple(map(int, input().split()))
   dq = collections.deque([t])
   print(asd(dq))