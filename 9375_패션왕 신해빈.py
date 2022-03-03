from sys import stdin
t=int(input())
for _ in range(t):
    dic={}
    n=int(input())
    for _ in range(n):
        s2=stdin.readline().split()[1]
        if s2 in dic:
            dic[s2]+=1
        else:
            dic[s2]=1
    l=dic.values()
    result=1
    for i in l:
        result*=(i+1)
    print(result-1)