s=input()

#숫자총합
sum=0

string=[]

for i in s:
    if i>='A' and i<='Z':
        string+=i
    if i>='0' and i<='9':
        sum+=int(i)

string.sort()

#join 문자열 변환 함수
print(''.join(string),end='')

if sum!=0:
    print(sum)
