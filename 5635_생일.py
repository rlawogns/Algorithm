n=int(input())
l=[]
for _ in range(n):
    l.append(list(input().split()))
l.sort(key=  lambda x : (int(x[3]),int(x[2]),int(x[1])))
print(l[n-1][0])
print(l[0][0])