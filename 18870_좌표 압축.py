from sys import stdin
n=int(input())
l=list(map(lambda x:[x[0],x[1]],enumerate(list(map(int,stdin.readline().split())))))
l.sort(key=lambda x : x[1])
rank=0
t=l[0][1]
for i in l:
    if t==i[1]:
        i[1]=rank
    else:
        rank+=1
        t=i[1]
        i[1]=rank
l.sort()
for i in l:
    print(i[1],end=' ')