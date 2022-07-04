#위에서 아래로

num=int(input())

num_list=[]

#리스트에 숫자 하나씩 입력하기
for i in range(num):
    num_list.append(int(input()))
#파이썬 기본 함수 이용해 정렬
num_list=sorted(num_list,reverse=True)

for i in num_list:
    print(i,end=' ')
