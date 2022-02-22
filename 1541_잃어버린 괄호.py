s=input()
q=0
zero=0
result=""
for i in s:
    if q and i=='-':
        result+=')'
        q = 0
    if zero and ('0'<=i<='9'):
        result=result[:-1]
    result+=i
    zero=0
    if i=='0':
        if len(result)>1 and ('0'<=result[-2]<='9'):
            continue
        zero=1
    elif i=='-':
        result+='('
        q=1
if q:
    result+=')'
print(eval(result))