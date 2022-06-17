#문자열 재정렬 알파벳은 오름차순정렬 숫자는 더해서 마지막에
s=input()

result=[]
value=0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        value+=int(i)

result.sort()

if value!=0:
    result.append(str(value))

    print(''.join(result))
