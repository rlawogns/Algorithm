import sys
n= input()
dic={}
for i in sys.stdin.readline().split():
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
m= input()
for i in sys.stdin.readline().split():
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')