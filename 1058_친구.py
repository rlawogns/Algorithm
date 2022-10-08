from sys import stdin
n=int(input())
isFriend=[[0]*n for _ in range(n)]
l=[stdin.readline().rstrip() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if l[i][j]=='Y' and i!=j:
            isFriend[i][j]=1
            isFriend[j][i]=1
            for k in range(n):
                if l[j][k]=='Y' and i!=k:
                    isFriend[i][k]=1
                    isFriend[k][i]=1
print(max(map(sum,isFriend)))