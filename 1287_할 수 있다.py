from sys import stdin
from collections import deque
s=stdin.readline().rstrip()
dq=deque([])
ac=0
bc=0
for i in s:
    if len(dq) == 0:
        if i=='+' or i=='-' or i=='*' or i=='/' or i==')':
            print('ROCK')
            exit()
        elif i=='(':
            dq.append(i)
            ac+=1
        else:
            dq.append(i)
    else:
        if i=='+' or i=='-' or i=='*' or i=='/':
            if dq[-1]=='(' or dq[-1]=='+' or dq[-1]=='-' or dq[-1]=='*' or dq[-1]=='/':
                print('ROCK')
                exit()
            else:   # ), number
                dq.append(i)
        elif i=='(':
            if dq[-1] == '+' or dq[-1]=='-' or dq[-1]=='*' or dq[-1]=='/':
                dq.append(i)
                ac+=1
            elif dq[-1]=='(':
                dq.append(i)
                ac+=1
            else:
                print('ROCK')
                exit()
        elif i==')':
            if bc>=ac:
                print('ROCK')
                exit()
            elif dq[-1] == '+' or dq[-1]=='-' or dq[-1]=='*' or dq[-1]=='/':
                print('ROCK')
                exit()
            else:
                dq.append(i)
                bc+=1
        else:   #number
            if dq[-1] == ')':
                print('ROCK')
                exit()
            else:
                dq.append(i)
if dq[-1] == '+' or dq[-1]=='-' or dq[-1]=='*' or dq[-1]=='/' or dq[-1]=='(':
    print('ROCK')
else:
    s=s.replace('/','//')
    if type(eval(s))==int:
        print(eval(s))
    else:
        print('ROCK')