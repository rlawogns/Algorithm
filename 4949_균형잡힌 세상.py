import sys
s=sys.stdin.readline()[:-1]
while s!=".":
    l=[0]
    for i in s:
        if i == "(":
            l.append(i)
        elif i == "[":
            l.append(i)
        elif i==")":
            if l[-1]=="(":
                del(l[-1])
            else:
                l.append(0)
                break
        elif i=="]":
            if l[-1] == "[":
                del (l[-1])
            else:
                l.append(0)
                break
    if len(l)==1:
        print("yes")
    else:
        print("no")
    s = sys.stdin.readline()[:-1]