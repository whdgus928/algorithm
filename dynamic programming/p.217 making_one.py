#1로 만들기

x=int(input())

#결과를 저장할 테이블 초기화
d=[0]*30001

for i in range(2,x+1):
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)

print(d[x])

#질문 d[1]값은 어디있는지 , elif/if 로 했을때 차이
