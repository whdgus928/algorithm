#그리디
#곱하기 혹은 더하기

s=input()

#결과 변수
result=int(s[0])

for i in range(1,len(s)):
    if s[i]=='0' or s[i]=='1' or result==0 or result==1:
        result+=int(s[i])
    else:
        result*=int(s[i])

print(result)
