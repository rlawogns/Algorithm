n=int(input())
s=input()
result=0
for i in range(len(s)):
    result+=(ord(s[i])-96)*pow(31,i)
print(result%1234567891)