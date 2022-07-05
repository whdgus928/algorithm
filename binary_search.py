#정렬된 배열에서 특정 수의 개수 구하기
n,x=map(int,input().split())

array=list(map(int,input().split()))

result=0

for i in array:
    if i==x:
        result+=1


if result==0:
    print(-1)
else:
    print(result)
