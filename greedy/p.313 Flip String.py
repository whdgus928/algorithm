s=input()

#0으로 바꾸는 횟수
count0=0
#1로 바꾸는 횟수
count1=0

if s[0]=='0':
    count1+=1
else:
    count0+=1

#두 번째 원소부터 확인
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        #다음수가 1로 변경된 경우
        if s[i+1]=='1':
            count0+=1
        else:
            count1+=1
        

print(min(count0,count1))
