from sys import stdin
n = int(stdin.readline().rstrip())
li = [int(stdin.readline().rstrip()) for _ in range(n)]
li.sort()
result=4
for i in li:
    f=0
    for j in range(i-4,i):
        if li.count(j)!=0:
            f+=1
    if result>(4-f):
        result=4-f
    f=0
    for j in range(i+1,i+5):
        if li.count(j)!=0:
            f+=1
    if result>(4-f):
        result=4-f
print(result)