from sys import stdin
n=int(input())
l=[list(map(int,stdin.readline().split())) for _ in  range(n)]
l.sort(key= lambda x : (x[1],x[0]))
result=0
pre=0
for i in l:
    if pre<=i[0]:
        result+=1
        pre=i[1]
print(result)