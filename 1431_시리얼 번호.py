from sys import stdin
def suml(x):
    num=0
    for i in x:
        if i.isdigit():
            num+=int(i)
    return num
n=int(input())
l=[stdin.readline().rstrip() for _ in range(n)]
l.sort(key= lambda x : (len(x),suml(x),x))
print(*l, sep='\n')