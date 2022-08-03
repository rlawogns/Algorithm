from sys import stdin
n=int(input())
result=0
for _ in range(n):
    s=stdin.readline().rstrip()
    l=set([])
    pre=''
    c=True
    for i in s:
        if(i in l):
            if pre!=i:
                c=False
                break
        else:
            pre=i
            l.add(i)
    if c:
        result+=1
print(result)
