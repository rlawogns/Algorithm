from sys import stdin
n=int(input())
l=[list(map(int,stdin.readline().split()))+[1] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        elif l[i][1]<l[j][1] and l[i][0]<l[j][0]:
            l[i][2]+=1
for i in l:
    print(i[2], end=' ')