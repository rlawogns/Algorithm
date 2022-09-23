import sys
n=int(input())
l=list(map(int,sys.stdin.readline().split()))
remove=int(input())
l[remove]=-2

def dfs(m):
    l[m]=-2
    for i in range(n):
        if m== l[i]:
            dfs(i)
result=0
dfs(remove)
for i in range(n):
    if i not in l and l[i]!=-2:
        result+=1
print(result)