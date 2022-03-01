from sys import stdin
n,m=map(int,input().split())
dic={}
for _ in range(n):
    net,pw=stdin.readline().split()
    dic[net]=pw
for _ in range(m):
    s=stdin.readline()[:-1]
    print(dic[s])