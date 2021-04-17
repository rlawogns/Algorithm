def move(x,y,m):
    if m=='R':
        x+=1
    elif m=='L':
        x-=1
    elif m=='B':
        y-=1
    elif m=='T':
        y+=1
    elif m=='RT':
        x+=1
        y+=1
    elif m=='LT':
        x-=1
        y+=1
    elif m=='RB':
        x+=1
        y-=1
    else:
        x-=1
        y-=1
    if 0<x<9 and 0<y<9:
        return x,y,0
    return kingi,kingj,1
king,dol,n=input().split()
kingi,kingj=ord(king[0])-64,int(king[1])
doli,dolj=ord(dol[0])-64,int(dol[1])
for i in range(int(n)):
    a=input()
    ti,tj,t=kingi,kingj,0
    kingi,kingj,k=move(kingi,kingj,a)
    if kingi==doli and kingj==dolj:
        doli,dolj,k=move(doli,dolj,a)
        if k==1:
            kingi,kingj=ti,tj
print(chr(kingi+64)+str(kingj))
print(chr(doli+64)+str(dolj))