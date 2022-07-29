l=list(input())
l.sort()
sl=sorted(list(set(l)))
oddChr=''
slCount=[]
result=''
for i in sl:
    t=l.count(i)
    if t%2==1 and oddChr=='':
        oddChr=i
    elif t%2==1 and oddChr!='':
        print("I'm Sorry Hansoo")
        exit()
    slCount.append(t)
for i in range(len(sl)):
    for j in range(slCount[i]//2):
        result+=sl[i]
result=result+oddChr+result[::-1]
print(result)